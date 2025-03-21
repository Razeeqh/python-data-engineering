from db.sql_server import get_sql_server_connection, fetch_data
import pandas as pd
from db.snowflake_db import get_snowflake_connection, load_data_to_snowflake  # Ensure correct import
from config import SNOWFLAKE_CONFIG

def main():
    # Establish SQL Server connection
    sql_conn = get_sql_server_connection()
    if sql_conn is None:
        return

    # Define your SQL query
    query = "SELECT * FROM dbo.DimCustomer;"

    # Fetch data from SQL Server
    data = fetch_data(query, sql_conn)
    if data is not None:
        print("Data fetched from SQL Server:")
        print(data.head())

        # Establish Snowflake connection
        snowflake_conn = get_snowflake_connection()
        if snowflake_conn is not None:
            # Load data into Snowflake
            load_data_to_snowflake(snowflake_conn, data, SNOWFLAKE_CONFIG['table_name'])
            # Close Snowflake connection
            snowflake_conn.close()
        else:
            print("Failed to connect to Snowflake.")
    else:
        print("No data fetched from SQL Server.")

    # Close SQL Server connection
    sql_conn.close()

if __name__ == "__main__":
    main()
