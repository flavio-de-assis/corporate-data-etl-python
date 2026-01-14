# Pipeline de Tratamento de Dados de Vendas

## 📌 Descrição
Este projeto implementa um pipeline de dados em Python para leitura, limpeza, padronização, tipagem e tratamento de um dataset de vendas, seguindo boas práticas de Engenharia de Dados.

O pipeline realiza desde a leitura de dados brutos (**raw**) até a geração de dados tratados (**processed**), prontos para análise, visualização ou carga em banco de dados.

---

## 🗂 Estrutura do Projeto

```
projeto_dados/
├── data/
│   ├── raw/
│   │   └── vendas_raw.csv
│   └── processed/
│       └── vendas_tratadas.csv
├── scripts/
│   └── ler_dados.py
└── README.md
```

---

## ⚙️ Tecnologias Utilizadas
- Python 3
- Pandas
- Pathlib
- Expressões Regulares (re)
- UnicodeData

---

## 🔄 Etapas do Pipeline

1. **Leitura dos dados brutos**
   - Leitura de arquivo CSV localizado em `data/raw`
   - Validação da existência do arquivo de entrada

2. **Padronização dos nomes das colunas**
   - Conversão para letras minúsculas
   - Remoção de espaços extras
   - Conversão para `snake_case`
   - Remoção de acentos e caracteres especiais

3. **Tratamento de valores textuais**
   - Remoção de espaços extras
   - Padronização para letras minúsculas
   - Tratamento seguro de valores nulos

4. **Tipagem de dados**
   - Conversão de colunas de data para o tipo `datetime`
   - Uso de `errors="coerce"` para garantir consistência

5. **Tratamento de valores nulos**
   - Remoção de registros essenciais inválidos
   - Preenchimento de valores numéricos com zero
   - Preenchimento de valores textuais com valor padrão
   - Remoção de colunas totalmente nulas

6. **Geração do dataset tratado**
   - Salvamento do arquivo final em `data/processed`
   - Dataset pronto para análise ou ingestão em banco de dados

---

## ▶️ Como Executar o Projeto

1. Clone o repositório ou copie o projeto para sua máquina.

2. (Opcional, recomendado) Crie e ative um ambiente virtual:
```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install pandas
```

4. Execute o pipeline:
```bash
cd scripts
py ler_dados.py
```

---

## 📈 Resultado

Ao final da execução, o arquivo abaixo será gerado automaticamente:

```
data/processed/vendas_tratadas.csv
```

Este arquivo contém os dados:
- Limpos
- Padronizados
- Tipados corretamente
- Prontos para análise ou carga em banco de dados

---

## 🎯 Objetivo do Projeto

Este projeto demonstra habilidades práticas em:

- Engenharia de Dados
- Construção de pipelines ETL
- Limpeza e padronização de dados
- Tratamento de valores nulos
- Organização de projetos em Python
- Boas práticas de validação de dados

---

## 📌 Observações

- Os dados brutos **não são alterados** durante o processo.
- Todas as transformações são realizadas pelo script `ler_dados.py`.
- O pipeline pode ser facilmente estendido para:
  - Cargas incrementais
  - Integração com bancos de dados
  - Orquestração com Airflow ou similares
