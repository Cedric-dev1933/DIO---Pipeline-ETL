# DIO---Pipeline-ETL

## Descrição
Este projeto tem como objetivo demonstrar um pipeline simples de ETL (Extract, Transform, Load) utilizando Python e a biblioteca Pandas.

Os dados dos clientes são extraídos de um arquivo CSV, transformados através de regras de classificação e recomendações personalizadas, e posteriormente carregados em um novo arquivo CSV contendo as informações processadas.

## Tecnologias Utilizadas
- Python
- Pandas

## Estrutura do Projeto
- `clientes.csv`
  - Arquivo original contendo os dados brutos dos clientes.

- `ETL.py`
  - Script responsável pelas etapas de Extract, Transform e Load.

- `clientes_transformados.csv`
  - Arquivo gerado após o processamento dos dados.

## Etapas do Pipeline ETL

### Extract
Leitura dos dados do arquivo CSV utilizando Pandas.

### Transform
Durante a transformação dos dados:
- Os nomes das colunas são padronizados;
- Os clientes são classificados em categorias;
- Recomendações financeiras personalizadas são geradas automaticamente, baseando-se em critérios de saldo bancário e idade.

### Load
Os dados transformados são salvos em um novo arquivo CSV.


## Como executar
# Instale a biblioteca Pandas, caso não a tenha ainda:
pip install pandas

# Execute o script
python ETL.py

# O arquivo clientes_transformados.csv será gerado automaticamente.
