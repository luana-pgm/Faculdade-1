# Faculdade - Projeto Terceiro Semestre
Desenvolvimento de dashboards de acordo com planilhas tratadas. Algumas informações como o nome das tabelas foram alterados para este projeto ser publicado, mediante os dados serem confidênciais. O intuito deste projeto no github é apenas demonstrar a estruturação que fizemos do código para subir para o Power BI

## Contexto do Proejeto
Pegamos arquivos inicialmente com nosso fornecedor de um projeto de extensão que estavamos desenvolvendo. Assim, desde o inicio seguimos a seguinte trilhas:

1 - Fizemos a trativa dos dados e planilhas (ETL) - Nesta etapa, são realizadas conexões com as fontes de dados para extrair,
transformar e armazenar as informações em um banco de dados. As
transformações alinham os dados aos KPIs e métricas levantados durante a análise
de requisitos. Utilizaremos Python e bibliotecas especializadas para o processo
ETL.

2 - Criação de Staging - A área de staging serve como uma réplica do ambiente de produção, permitindo
testes e ajustes antes do carregamento dos dados no Data Warehouse. Nesta fase
intermediária, serão realizadas as transformações finais, incluindo a limpeza e
padronização dos dados, para adequá-los ao modelo de dados do Data Warehouse.

3 - Armazenamento no Data Warehouse - Após as transformações, os dados são carregados no Data Warehouse, que se torna
o repositório centralizado e estruturado de informações. O DW armazena grandes
volumes de dados de forma organizada, otimizando sua recuperação e análise para
apoiar decisões estratégicas. Nesta fase, o Airbyte mantém a infraestrutura, e os
dados são armazenados de acordo com o modelo definido, assegurando
consistência e integridade.

4 - Visualização dos Dado - Os dados no Data Warehouse são então disponibilizados para ferramentas de
Business Intelligence (neste caso, Power BI), transformando-os em visualizações
que facilitam a análise de KPIs e métricas do projeto. Esta etapa permite que os
usuários interajam com os dados dinamicamente, gerando insights relevantes para
a tomada de decisão.

## Considerações
Mediante o apresentado, deixo para vocês nossos arquivos finais

