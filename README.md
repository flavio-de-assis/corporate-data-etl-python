# ETL – Pipeline de Dados em Python e SQL

Este projeto demonstra a construção de um pipeline ETL (Extract, Transform, Load)
utilizando Python e SQL, simulando um cenário comum em ambientes corporativos
orientados a dados.

O objetivo é consolidar dados de origem estruturada em uma base padronizada,
permitindo análises confiáveis, automatizadas e reproduzíveis.

---

## Contexto

Em empresas orientadas por dados, informações costumam estar distribuídas em
diferentes fontes e formatos. Processos manuais de consolidação aumentam o risco
de erros, retrabalho e inconsistência nos dados utilizados para análise e tomada
de decisão.

Pipelines ETL são fundamentais para garantir que os dados estejam organizados,
confiáveis e prontos para consumo analítico.

---

## Problema

Havia a necessidade de extrair dados de uma fonte estruturada, aplicar
transformações e regras de padronização, e carregar os dados tratados em uma base
final preparada para análises posteriores.

O processo precisava ser automatizado, organizado e de fácil manutenção,
simulando um fluxo real de Engenharia de Dados.

---

## Solução Implementada

Foi desenvolvido um pipeline ETL utilizando Python e SQL, responsável por:

- Extração de dados da fonte de origem
- Transformação, limpeza e padronização dos dados
- Conversão de tipos e organização das informações
- Carga dos dados tratados em uma base final para análise

O pipeline foi estruturado de forma modular, facilitando leitura, manutenção e
possíveis evoluções futuras.

---

## Impacto

Este pipeline permite:

- Redução de retrabalho manual
- Padronização dos dados utilizados em análises
- Base confiável para relatórios e dashboards
- Melhor suporte à tomada de decisão baseada em dados

---

## Tecnologias Utilizadas

- Python
- SQL
- Pandas
- Ambiente local

---

## Estrutura do Projeto e Execução

```text
etl-pipeline-python/
├── data/                # Dados de entrada e/ou saída do pipeline
├── src/                 # Código-fonte do pipeline ETL
│   ├── extract/         # Lógica de extração dos dados
│   ├── transform/       # Transformação e limpeza dos dados
│   └── load/            # Carga dos dados tratados
├── requirements.txt     # Dependências do projeto
├── run_etl.py           # Script principal de execução do pipeline
└── README.md

# COMO EXECUTAR O PROJETO

# 1. Clone o repositório
git clone https://github.com/flavio-de-assis/etl-pipeline-python.git

# 2. Acesse o diretório do projeto
cd etl-pipeline-python

# 3. (Opcional) Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows

# 4. Instale as dependências
pip install -r requirements.txt

# 5. Execute o pipeline
python run_etl.py

# EXEMPLO DE SAÍDA ESPERADA

INFO: Iniciando pipeline ETL
INFO: Extração concluída com sucesso
INFO: Transformações aplicadas
INFO: Dados carregados com sucesso
INFO: Pipeline finalizado
```

---

## Possíveis Evoluções

Este projeto pode ser evoluído para um ambiente de produção com:

- Orquestração do pipeline utilizando Airflow ou Prefect
- Containerização com Docker
- Monitoramento de falhas e reprocessamento automático
- Testes automatizados para validação da qualidade dos dados
- Integração com ambientes de cloud (AWS, GCP ou Azure)

---

## Observações

Este projeto foi desenvolvido com foco educacional e demonstrativo, buscando
representar desafios reais encontrados em pipelines de dados corporativos e boas
práticas iniciais de Engenharia de Dados.
