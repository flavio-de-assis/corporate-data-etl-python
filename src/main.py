# ============================
# IMPORTS
# ============================

# Manipulação de caminhos e arquivos
from pathlib import Path

# Biblioteca principal para manipulação de dados
import pandas as pd

# Utilizada para normalização de caracteres (acentuação)
import unicodedata

# Utilizada para limpeza de strings com expressões regulares
import re


# ============================
# DEFINIÇÃO DE CAMINHOS
# ============================

# Diretório base do projeto (um nível acima do diretório atual)
BASE_DIR = Path(__file__).resolve().parent.parent

# Caminho do arquivo de dados brutos (raw)
ARQUIVO_RAW = BASE_DIR / "data" / "raw" / "vendas_raw.csv"

# Validação da existência do arquivo de entrada
# Evita falhas silenciosas durante a execução do pipeline
if not ARQUIVO_RAW.exists():
    raise FileNotFoundError(
        f"Arquivo de entrada não encontrado: {ARQUIVO_RAW}"
    )


# ============================
# LEITURA DOS DADOS RAW
# ============================

# Leitura do arquivo CSV bruto
# O separador é ';' conforme padrão do arquivo de origem
df = pd.read_csv(ARQUIVO_RAW, sep=";")


# ============================
# PADRONIZAÇÃO DOS NOMES DAS COLUNAS
# ============================

def padronizar_colunas(colunas):
    """
    Padroniza nomes de colunas para um formato consistente:
    - Letras minúsculas
    - Remoção de espaços
    - Remoção de acentuação
    - Apenas caracteres alfanuméricos e underscore
    """

    colunas_padronizadas = []

    for col in colunas:
        col = col.lower()
        col = col.strip()
        col = col.replace(" ", "_")
        col = unicodedata.normalize("NFKD", col)
        col = col.encode("ascii", "ignore").decode("utf-8")
        col = re.sub(r"[^a-z0-9_]", "", col)

        colunas_padronizadas.append(col)

    return colunas_padronizadas


# Aplicação da padronização aos nomes das colunas
df.columns = padronizar_colunas(df.columns)


# ============================
# PADRONIZAÇÃO DE VALORES TEXTUAIS
# ============================

# Identificação de colunas do tipo texto
colunas_texto = df.select_dtypes(include=["object", "string"]).columns

# Limpeza dos valores textuais:
# - Remoção de espaços
# - Conversão para minúsculas
# - Preservação de valores nulos
for col in colunas_texto:
    df[col] = df[col].apply(
        lambda x: str(x).strip().lower() if pd.notna(x) else x
    )


# ============================
# TIPAGEM DE COLUNAS DE DATA
# ============================

# Lista de colunas que representam datas no domínio do negócio
colunas_data = [
    "dtvenda",
    "dtestorno",
    "dtaltera",
    "criacaofinalizada",
]

# Conversão segura para datetime
# Valores inválidos são convertidos para NaT
for col in colunas_data:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors="coerce")


# ============================
# REMOÇÃO DE REGISTROS ESSENCIAIS NULOS
# ============================

# Campos obrigatórios para integridade do dado
colunas_essenciais = ["cdvenda", "cdcliente", "dtvenda"]

# Remove registros que não possuem informações mínimas essenciais
df = df.dropna(subset=colunas_essenciais)


# ============================
# TRATAMENTO DE VALORES NUMÉRICOS NULOS
# ============================

# Colunas numéricas que devem assumir zero quando ausentes
colunas_numericas = [
    "valorfretecte",
    "valorusadovalecompra",
    "valoraproximadoimposto",
]

# Preenchimento de valores nulos com 0
for col in colunas_numericas:
    if col in df.columns:
        df[col] = df[col].fillna(0)


# ============================
# TRATAMENTO DE VALORES TEXTUAIS NULOS
# ============================

# Colunas textuais onde ausência de valor é relevante
colunas_texto_nulo = [
    "observacao",
    "observacaointerna",
]

# Preenchimento de valores nulos com marcador padrão
for col in colunas_texto_nulo:
    if col in df.columns:
        df[col] = df[col].fillna("nao_informado")


# ============================
# REMOÇÃO DE COLUNAS COMPLETAMENTE NULAS
# ============================

# Remove colunas sem nenhum valor útil
df = df.dropna(axis=1, how="all")


# ============================
# VALIDAÇÃO E INSPEÇÃO DOS DADOS
# ============================

# Exibe amostra dos dados tratados
print(df.head())

# Exibe informações estruturais do DataFrame
print(df.info())

# Lista final de colunas após tratamento
print(df.columns)


# ============================
# SALVAMENTO DOS DADOS TRATADOS
# ============================

# Diretório de saída para dados processados
OUTPUT_DIR = BASE_DIR / "data" / "processed"

# Cria o diretório caso não exista
OUTPUT_DIR.mkdir(exist_ok=True)

# Caminho do arquivo final tratado
OUTPUT_FILE = OUTPUT_DIR / "vendas_tratadas.csv"

# Escrita do DataFrame tratado em CSV
df.to_csv(OUTPUT_FILE, index=False, sep=";")

# Log simples de sucesso
print(f"Arquivo tratado salvo em: {OUTPUT_FILE}")
