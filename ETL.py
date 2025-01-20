import pandas as pd
import psycopg2

## Importando tabela de unidades e selecionando colunas definidas na modelagem

panarama_geral_filepath = 'raw_data/EXTRATO - ESTABELECIMENTOS + LEITOS.csv'
df_unidades_saude = pd.read_csv(panarama_geral_filepath)
df_unidades_saude_cols_selecionadas = df_unidades_saude[['CNES', 'NOME␣
↪FANTASIA', 'LOGRADOURO', 'BAIRRO']]
df_unidades_saude_cols_selecionadas.head()

## Importando tabela de equipes e selecionando colunas desejadas

profissionais_equipes_filepath = 'raw_data/CNES - EXTRATO PROFISSIONAIS SUS.csv'
df_equipes = pd.read_csv(profissionais_equipes_filepath)
df_equipes_colunas_selecionadas = df_equipes[['equipe_ine', 'equipe_nome',␣
↪'TIPO EQUIPE', 'equipe_dt_ativacao', 'equipe_dt_desativacao']]
df_equipes_colunas_selecionadas.head()


## Importando tabela de profissionais e selecionando colunas desejadas

: df_profissionais = pd.read_csv(profissionais_equipes_filepath)
df_profissionais_colunas_selecionadas =␣
↪df_profissionais[['cnes','profissional_cns', 'profissional_cbo',␣
↪'profissional_nome', 'equipe_dt_entrada', 'equipe_dt_desligamento']]
df_profissionais_colunas_selecionadas.head()


## Importando tabela fato

fato_atendimentos_filepath = 'raw_data/atendimentos.xlsx'
df_fato_atendimentos = pd.read_excel(fato_atendimentos_filepath)


## Criando funçào para normalizar nome das colunas

def normalize_columns(df):
if df is None:
print("Input DataFrame is None")
return None
df.columns = (
df.columns
.str.encode('ascii', errors='ignore') # Remover acentos
.str.decode('utf-8')
.str.replace(' ', '_')
.str.lower()
)
print("Normalized column names:", df.columns.tolist())
return df


## Chamando funcao normalize_columns

normalize_columns(df_unidades_saude_cols_selecionadas)

normalize_columns(df_equipes_colunas_selecionadas)

normalize_columns(df_profissionais_colunas_selecionadas)

normalize_columns(df_fato_atendimentos)


## Criando conexao com o banco de dados Postgres

try:
conn = psycopg2.connect("host=localhost port=5257 dbname=db_fonte user=puc␣password=puc")
print("Connected!")
except psycopg2.Error as e:
print(e)


## Criando cursor para o banco de dados

try:
cur = conn.cursor()
except psycopg2.Error as e:
print(e)


## Criando cursor para o banco de dados

try:
cur = conn.cursor()
except psycopg2.Error as e:
print(e)


##  Criando schema e carregando tabelas no banco de dados

schema_name = 'fonte'
try:
cur.execute(f"CREATE SCHEMA IF NOT EXISTS {schema_name};")
conn.commit()
print(f"Schema '{schema_name}' criado com sucesso ou já existe.")
except psycopg2.Error as e:
conn.rollback()
print(f"Erro ao criar o schema '{schema_name}': {e}")


## Carregando tabelas no banco de dados

from sqlalchemy import create_engine
# Configurando a string de conexão
engine = create_engine("postgresql+psycopg2://puc:puc@localhost:5257/db_fonte")
# Salvando os DataFrames no schema especificado
df_unidades_saude_cols_selecionadas.to_sql('unidades_saude', engine,␣
↪schema=schema_name, if_exists='replace', index=False)
df_equipes_colunas_selecionadas.to_sql('equipes', engine, schema=schema_name,␣
↪if_exists='replace', index=False)
df_fato_atendimentos.to_sql('atendimentos', engine, schema=schema_name,␣
↪if_exists='replace', index=False)
df_profissionais_colunas_selecionadas.to_sql('profissionais', engine,␣
↪schema=schema_name, if_exists='replace', index=False)
print("Tabela inseridas no banco de dados com sucesso!")
# Fecha a conexão
engine.dispose()


## Fecha a conexao com o banco de dados

cur.close()
conn.close()










