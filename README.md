
# Data Warehouse - Star Schema (Sales)

Projeto: Data Warehouse bem estruturado com STAR SCHEMA para análise de vendas.

## Conteúdo do projeto
- `raw_sales.csv` : dados transacionais brutos (simulados)
- `etl_build_dw.py` : script Python de ETL que gera dimensões, fato e cria um arquivo SQLite (data_warehouse.db)
- `dw_dim_date.csv`, `dw_dim_customer.csv`, `dw_dim_product.csv`, `dw_dim_store.csv` : CSVs gerados pelo ETL
- `dw_fact_sales.csv` : tabela fato gerada pelo ETL
- `data_warehouse.db` : banco SQLite com as tabelas já carregadas (gerado após rodar o ETL)
- `ddl_star_schema.sql` : DDL para criar o schema em qualquer SGBD
- `dw_analytics_queries.sql` : Queries de análise (top produtos, receita mensal, etc.)

## Como executar (local)
1. Gere o ambiente (recomendado criar um venv):
   ```
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate    # Windows
   pip install pandas sqlite3
   ```

2. Rode o ETL:
   ```
   python etl_build_dw.py
   ```

   Isso criará os arquivos `dw_*.csv` e `data_warehouse.db`.

3. Use o arquivo `data_warehouse.db` com qualquer cliente SQLite (DBeaver, DB Browser for SQLite, etc.)
   ou adapte `ddl_star_schema.sql` para seu SGBD (Postgres, MySQL).

## Sugestões de próximos passos
- Conectar o `data_warehouse.db` no Power BI para criar dashboards.
- Criar índices e analisar performance com EXPLAIN ANALYZE no seu SGBD.
- Expandir dimensões (ex: dim_promo, dim_employee) e criar fatos adicionais.
