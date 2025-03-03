import pandas as pd
import sqlite3
from sqlalchemy import create_engine, Column, Integer, String, Float, MetaData, Table


def csv_to_sql(csv_file_path, connection_string, table_name, table_initalization_query):
    ''' Reads the csv file and puts it into the sql table.

    Args: csv_file_path: str - The path to the csv file
    connection_string: str - The connection string to the database
    table_name: str - The name of the table to be created
    table_initalization_query: str - The query to initialize the table

    Returns: None

    '''

    # Connecting to the Dataframe from CSV File path
    print(f"Reading csv file from {csv_file_path}")
    df = pd.read_csv(csv_file_path)

    # Connecting to the Database or Creating a new one if it doesn't exist.
    database = sqlite3.connect(connection_string)
    cursor = database.cursor()

    cursor.execute(table_initalization_query)
    database.commit()
    print(f"Connected to database {connection_string}")

    # Removed the unnamed 0 column from the dataframe
    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'], inplace=True)

    ############################################################
    # Insert Test cases for Valid Dataframe here
    ############################################################

    # Writing the dataframe to the Database
    df.to_sql(table_name, database, if_exists='append', index=False)

    # Test Reading data from the Database
    query = f"SELECT * FROM {table_name}"
    df_from_db = pd.read_sql_query(query, database)
    print(df_from_db.head())

    # Close the Database and Return
    database.close()
    print("Successful creation of SQLite DB from Dataframe")
