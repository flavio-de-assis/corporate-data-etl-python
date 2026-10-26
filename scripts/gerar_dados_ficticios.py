# ============================
# GERAÇÃO DA BASE FICTÍCIA
# ============================

# Gera data/raw/vendas_raw.csv com dados 100% fictícios, no mesmo
# layout (76 colunas) de uma exportação de vendas de ERP.
# A semente fixa garante que o arquivo seja sempre o mesmo.

import csv
import random
from datetime import date, datetime, timedelta
from pathlib import Path

random.seed(42)

BASE_DIR = Path(__file__).resolve().parent.parent
ARQUIVO_SAIDA = BASE_DIR / "data" / "raw" / "vendas_raw.csv"

COLUNAS = (
    "cdvenda;cdempresa;cdcliente;cdcolaborador;dtvenda;dtestorno;dtaltera;cdusuarioaltera;"
    "cdenderecoentrega;orcamento;observacao;cdvendasituacao;cdconta;cdindicecorrecao;valorfrete;"
    "frete;cdterceiro;cdformapagamento;cdprazopagamento;cdpedidovenda;identificadorexterno;desconto;"
    "prazomedio;saldofinal;cdprojeto;identificadorcarregamento;bonificacao;taxavenda;"
    "cdlocalarmazenagem;identificador;expedicaovendasituacao;taxapedidovenda;cdmaterialtabelapreco;"
    "percentualdesconto;cdclienteindicacao;qtdeparcelas;cdvendaorcamento;observacaointerna;"
    "cdclientevalecompra;comodato;cdcontato;valorusadovalecompra;cdpedidovendatipo;origemwebservice;"
    "cdfornecedor;percentualrepresentacao;cdprazopagamentorepresentacao;cdformapagamentorepresentacao;"
    "cdcontarepresentacao;valorbrutorepresentacao;valordescontorepresentacao;presencacompradornfe;"
    "criacaofinalizada;aprovando;valoraproximadoimposto;limitecreditoexcedido;cdcentrocusto;"
    "valorfretecif;origemotr;cdenderecofaturamento;vendapendencianaonegociada;quantidadevolumes;"
    "sinalizadosemreserva;expedicaosituacao;cdparceiro;entregaecommercerealizada;intermediadornfe;"
    "cdintermediador;cdclienteremessa;incideiss;numeropedido;nsu;codigoautorizacao;operacaonfe;"
    "valorfretecte;emailautomaticofaturamentoenviadovendarealizada"
).split(";")

# Textos livres com problemas típicos de digitação (espaços, caixa misturada)
OBSERVACOES = [
    "  Entregar no período da manhã ",
    "CLIENTE PEDIU NOTA FISCAL SEPARADA",
    "Ligar antes de entregar",
    "Retirada no balcão ",
]
OBSERVACOES_INTERNAS = [
    "Conferir cadastro do cliente ",
    "  PRIORIDADE ALTA",
    "Aguardando aprovação do financeiro",
]

QTD_VENDAS = 220
CLIENTES = random.sample(range(100, 999), 60)
COLABORADORES = [11, 12]
USUARIOS = [101, 102, 103]


def data_br(d):
    return d.strftime("%d/%m/%Y")


def gerar_linha(i):
    linha = {coluna: "" for coluna in COLUNAS}

    cliente = random.choice(CLIENTES)
    dia_venda = date(2025, 1, 2) + timedelta(days=random.randint(0, 180))

    linha["cdvenda"] = 10001 + i
    linha["cdempresa"] = random.choice([1, 2, 3])
    linha["cdcliente"] = cliente
    linha["cdcolaborador"] = random.choice(COLABORADORES) if random.random() > 0.04 else ""
    linha["dtvenda"] = data_br(dia_venda)

    if random.random() > 0.05:
        alteracao = datetime.combine(dia_venda, datetime.min.time()) + timedelta(
            hours=random.randint(8, 18), minutes=random.randint(0, 59)
        )
        linha["dtaltera"] = alteracao.strftime("%d/%m/%Y %H:%M")

    linha["cdusuarioaltera"] = random.choice(USUARIOS)
    linha["cdenderecoentrega"] = cliente + 1000 if random.random() > 0.03 else ""
    if random.random() < 0.06:
        linha["observacao"] = random.choice(OBSERVACOES)
    linha["cdvendasituacao"] = random.choice([0, 2, 2, 2, 5])
    if random.random() < 0.35:
        linha["cdconta"] = random.choice([1, 2, 3])
    linha["valorfrete"] = random.choice([0, 0, 0, 15.9, 32.5])
    linha["frete"] = random.choice([1, 2])
    linha["cdformapagamento"] = random.choice([1, 2, 3])
    linha["cdprazopagamento"] = random.randint(10, 25)
    linha["cdpedidovenda"] = 20001 + i
    linha["desconto"] = random.choice([0, 0, 0, 5, 10])
    linha["prazomedio"] = "false"
    linha["bonificacao"] = "false"
    linha["taxavenda"] = 0
    linha["cdlocalarmazenagem"] = random.choice([1, 2])
    linha["identificador"] = 3001 + i
    if random.random() < 0.1:
        linha["percentualdesconto"] = random.choice([2, 5])
    if random.random() < 0.05:
        linha["observacaointerna"] = random.choice(OBSERVACOES_INTERNAS)
    linha["comodato"] = "false"
    if random.random() < 0.35:
        linha["cdcontato"] = cliente + 5000
    if random.random() < 0.04:
        linha["valorusadovalecompra"] = random.choice([20, 50])
    linha["cdpedidovendatipo"] = 1
    linha["valorbrutorepresentacao"] = 0
    linha["valordescontorepresentacao"] = 0
    linha["presencacompradornfe"] = random.choice([1, 4])
    linha["criacaofinalizada"] = random.choice(["true", "false"])
    if random.random() < 0.3:
        linha["valoraproximadoimposto"] = round(random.uniform(10, 400), 2)
    linha["valorfretecif"] = 0
    linha["sinalizadosemreserva"] = "false"
    linha["intermediadornfe"] = 0
    linha["operacaonfe"] = 0
    if random.random() < 0.1:
        linha["valorfretecte"] = round(random.uniform(5, 60), 2)
    linha["emailautomaticofaturamentoenviadovendarealizada"] = random.choice(["false", "true"])

    return linha


linhas = [gerar_linha(i) for i in range(QTD_VENDAS)]

# Problemas de qualidade inseridos de propósito, para o pipeline tratar
linhas[15]["dtvenda"] = "31/02/2025"  # data que não existe
linhas[48]["dtvenda"] = "0"           # data inválida
linhas[97]["dtvenda"] = ""            # data ausente
linhas[120]["cdcliente"] = ""         # venda sem cliente
linhas[171]["cdcliente"] = ""
linhas[203]["cdvenda"] = ""           # venda sem código

ARQUIVO_SAIDA.parent.mkdir(parents=True, exist_ok=True)
with open(ARQUIVO_SAIDA, "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.DictWriter(arquivo, fieldnames=COLUNAS, delimiter=";")
    escritor.writeheader()
    escritor.writerows(linhas)

print(f"{len(linhas)} vendas fictícias gravadas em: {ARQUIVO_SAIDA}")
