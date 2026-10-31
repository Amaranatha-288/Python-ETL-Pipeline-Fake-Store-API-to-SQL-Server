from sqlalchemy import create_engine
from sqlalchemy.engine import URL

# SQL Server connection details
server = r'localhost\SQLEXPRESS'
database = 'fake_store_db'


def load_to_sqlserver(df, table_name):

    connection_url = URL.create(
        'mssql+pyodbc',
        host=server,
        database=database,
        query={
            'driver': 'ODBC Driver 18 for SQL Server',
            'Trusted_Connection': 'yes',
            'TrustServerCertificate': 'yes'
        }
    )

    engine = create_engine(connection_url)

    try:
        with engine.begin() as connection:
            df.to_sql(
                name=table_name,
                con=connection,
                if_exists='replace',
                index=False
            )

        print(f'Data loaded into SQL Server table: {table_name}')

    finally:
        engine.dispose()