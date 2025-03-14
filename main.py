from db.sql_server import get_sql_server_connection, fetch_data
import pyodbc
import pandas as pd

def main():
    # Establish connection
    conn = get_sql_server_connection()
    if conn is None:
        return

    # Define your SQL query
    query = "SELECT * FROM dbo.DimCustomer;"

    # Fetch data
    data = fetch_data(query, conn)
    if data is not None:
        print(data.head())

    # Close the connection
    conn.close()

if __name__ == "__main__":
    main()
