import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
from config import SNOWFLAKE_CONFIG

def get_snowflake_connection():
    try:
        conn = snowflake.connector.connect(
            user=SNOWFLAKE_CONFIG['user'],
            password=SNOWFLAKE_CONFIG['password'],
            account=SNOWFLAKE_CONFIG['account'],
            warehouse=SNOWFLAKE_CONFIG['warehouse'],
            database=SNOWFLAKE_CONFIG['database'],
            schema=SNOWFLAKE_CONFIG['schema'],
            role=SNOWFLAKE_CONFIG['role']
        )
        return conn
    except snowflake.connector.Error as e:
        print(f"Error connecting to Snowflake: {e}")
        return None

def load_data_to_snowflake(connection, df, table_name):
    try:
        success, nchunks, nrows, _ = write_pandas(connection, df, table_name, auto_create_table=True)
        if success:
            print(f"Successfully loaded {nrows} rows into {table_name}.")
        else:
            print("Data load into Snowflake failed.")
    except Exception as e:
        print(f"Error loading data to Snowflake: {e}")
