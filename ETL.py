import pandas as pd
import psycopg2

### Importando tabela de unidades e selecionando colunas definidas na modelagem

panarama_geral_filepath = 'raw_data/EXTRATO - ESTABELECIMENTOS + LEITOS.csv'
df_unidades_saude = pd.read_csv(panarama_geral_filepath)
df_unidades_saude_cols_selecionadas = df_unidades_saude[['CNES', 'NOME␣
↪FANTASIA', 'LOGRADOURO', 'BAIRRO']]
df_unidades_saude_cols_selecionadas.head()

