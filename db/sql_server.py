import pyodbc
import pandas as pd

def get_sql_server_connection():
    """
    Establishes and returns a connection to the SQL Server.
    """
    conn_str = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=JARVIS;"
        "DATABASE=AdventureWorksDW2022;"
        "UID=IICS_SQL;"
        "PWD=IICS_SQL;"
    )
    try:
        conn = pyodbc.connect(conn_str)
        print("Connection to SQL Server established successfully.")
        return conn
    except pyodbc.Error as e:
        print(f"Error connecting to SQL Server: {e}")
        return None

def fetch_data(query, conn):
    """
    Executes the given SQL query and returns the result as a pandas DataFrame.
    """
    try:
        df = pd.read_sql(query, conn)
        return df
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None
