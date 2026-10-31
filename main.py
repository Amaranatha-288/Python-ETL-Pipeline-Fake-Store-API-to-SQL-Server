from etl.extract import extract_product, extract_users
from etl.transform import transform_product, transform_users
from etl.load import load_to_sqlserver


def run_pipeline():
    print('Starting pipeline')

    # Extract data
    product_df = extract_product()
    user_df = extract_users()

    print('Starting transformation')

    # Transform data
    product_df = transform_product(product_df)
    user_df = transform_users(user_df)

    print('Loading to SQL Server')

    # Load data into SQL Server
    load_to_sqlserver(product_df, 'products')
    load_to_sqlserver(user_df, 'users')

    print('ETL pipeline completed')


if __name__ == '__main__':
    run_pipeline()