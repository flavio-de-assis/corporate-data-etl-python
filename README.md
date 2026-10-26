# Corporate Data ETL Pipeline with Python

## 📌 Contexto do Negócio

Dados exportados de sistemas ERP raramente chegam prontos para análise: nomes de colunas inconsistentes, acentuação misturada, datas em formatos diferentes, campos vazios e registros incompletos.

Este projeto trata uma base de vendas no layout de exportação de um ERP (76 colunas), levando o dado da camada **bruta** (`raw`) para a camada **tratada** (`processed`), pronta para análises, relatórios ou carga em banco.

> **Dados 100% fictícios.** A base bruta é gerada pelo script `scripts/gerar_dados_ficticios.py` (semente fixa), com problemas de qualidade inseridos de propósito: data inexistente (`31/02/2025`), data inválida, vendas sem cliente ou sem código, textos com espaços e caixa misturada.

---

## 🎯 O que o pipeline faz

O script `src/main.py` executa, em sequência:

1. **Extração:** lê o CSV bruto de `data/raw/vendas_raw.csv` (separador `;`) e interrompe a execução com erro claro se o arquivo não existir.
2. **Padronização das colunas:** nomes em minúsculas, sem espaços, sem acentos e só com letras, números e `_`.
3. **Limpeza de texto:** remove espaços nas pontas e converte para minúsculas, preservando os nulos.
4. **Tipagem de datas:** converte `dtvenda`, `dtestorno`, `dtaltera` e `criacaofinalizada` para data no padrão brasileiro (`dayfirst=True`); valores inválidos viram nulo (`errors="coerce"`) em vez de quebrar o processo.
5. **Registros essenciais:** descarta linhas sem `cdvenda`, `cdcliente` ou `dtvenda`.
6. **Nulos com regra de negócio:** valores monetários ausentes viram `0`; observações ausentes viram `nao_informado`.
7. **Colunas vazias:** remove as colunas sem nenhum valor preenchido.
8. **Gravação:** salva o resultado em `data/processed/vendas_tratadas.csv` e exibe um resumo (`head`, `info` e lista de colunas) para conferência.

**Resultado:** a base passa de **76 para 38 colunas** úteis e de **220 para 214 vendas** (as 6 sem informação essencial são descartadas), com tipos e textos padronizados.

---

## 🛠️ Tecnologias

- Python 3
- pandas
- `pathlib`, `unicodedata` e `re` (biblioteca padrão)

---

## 📁 Estrutura do Projeto

```
corporate-data-etl-python/
├── data/
│   ├── raw/
│   │   └── vendas_raw.csv          # dado bruto, como sai do ERP
│   └── processed/
│       └── vendas_tratadas.csv     # dado tratado gerado pelo pipeline
├── scripts/
│   └── gerar_dados_ficticios.py    # gera a base bruta fictícia
├── src/
│   └── main.py                     # pipeline completo (extração, tratamento e gravação)
├── requirements.txt
└── README.md
```

---

## ⚙️ Como Executar

Na raiz do projeto:

```bash
python -m venv .venv
.venv\Scripts\activate          # no Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python src/main.py
```

O arquivo tratado é gravado em `data/processed/vendas_tratadas.csv`. Para recriar a base bruta do zero, rode antes `python scripts/gerar_dados_ficticios.py`.

---

## 🧠 Aprendizados

- Separar o dado bruto do dado tratado em camadas (`raw` → `processed`).
- Tratar datas inválidas sem interromper o pipeline.
- Definir regras explícitas para nulos conforme o significado de cada campo.
- Padronizar nomes de colunas para facilitar o uso em SQL e em ferramentas de BI.

---

## 🚀 Próximos Passos

- Separar as etapas em módulos (`extract.py`, `transform.py`, `load.py`).
- Carregar o resultado em um banco relacional (PostgreSQL) em vez de CSV.
- Trocar os `print` por logs com a contagem de linhas descartadas em cada etapa.
- Criar testes automatizados para as regras de tratamento.
- Agendar a execução com um orquestrador.

---

## 📄 Licença

Este projeto está sob a licença MIT e pode ser utilizado para fins educacionais ou profissionais.
