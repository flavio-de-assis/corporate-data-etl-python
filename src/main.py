# IMPORTS
from pathlib import Path
import pandas as pd
import unicodedata
import re

# CAMINHO BASE DO PROJETO
BASE_DIR = Path(__file__).resolve().parent.parent
ARQUIVO_RAW = BASE_DIR / "data" / "raw" / "vendas_raw.csv"
if not ARQUIVO_RAW.exists():
    raise FileNotFoundError(
        f"Arquivo de entrada não encontrado: {ARQUIVO_RAW}"
    )

# LEITURA DOS DADOS BRUTOS (RAW)
df = pd.read_csv(ARQUIVO_RAW, sep=";")

# PADRONIZAÇÃO DOS NOMES DAS COLUNAS
def padronizar_colunas(colunas):
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


df.columns = padronizar_colunas(df.columns)

# PADRONIZAÇÃO DE VALORES TEXTUAIS
colunas_texto = df.select_dtypes(include=["object", "string"]).columns

for col in colunas_texto:
    df[col] = df[col].apply(
        lambda x: str(x).strip().lower() if pd.notna(x) else x
    )

# TIPAGEM DE DATAS
colunas_data = [
    "dtvenda",
    "dtestorno",
    "dtaltera",
    "criacaofinalizada",
]

for col in colunas_data:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors="coerce")

# REMOÇÃO DE REGISTROS ESSENCIAIS NULOS
colunas_essenciais = ["cdvenda", "cdcliente", "dtvenda"]
df = df.dropna(subset=colunas_essenciais)

# PREENCHIMENTO DE NULOS NUMÉRICOS COM 0
colunas_numericas = [
    "valorfretecte",
    "valorusadovalecompra",
    "valoraproximadoimposto",
]

for col in colunas_numericas:
    if col in df.columns:
        df[col] = df[col].fillna(0)

# PREENCHIMENTO DE NULOS TEXTUAIS
colunas_texto_nulo = [
    "observacao",
    "observacaointerna",
]

for col in colunas_texto_nulo:
    if col in df.columns:
        df[col] = df[col].fillna("nao_informado")

# REMOÇÃO DE COLUNAS TOTALMENTE NULAS
df = df.dropna(axis=1, how="all")

# VALIDAÇÃO
print(df.head())
print(df.info())
print(df.columns)


# SALVAMENTO DOS DADOS TRATADOS
OUTPUT_DIR = BASE_DIR / "data" / "processed"
OUTPUT_DIR.mkdir(exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "vendas_tratadas.csv"

df.to_csv(OUTPUT_FILE, index=False, sep=";")

print(f"Arquivo tratado salvo em: {OUTPUT_FILE}")
