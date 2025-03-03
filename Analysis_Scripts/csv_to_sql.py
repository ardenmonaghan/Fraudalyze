import pandas as pd
import sqlite3
from sqlalchemy import create_engine, Column, Integer, String, Float, MetaData, Table


def csv_to_sql(csv_file_path, connection_string, table_name, table_initalization_query):
    ''' Reads the csv file and puts it into the sql table.'''

    print(f"Reading csv file from {csv_file_path}")
    df = pd.read_csv(csv_file_path)

    database = sqlite3.connect(connection_string)
    cursor = database.cursor()

    cursor.execute(table_initalization_query)
    database.commit()

    print(f"Connected to database {connection_string}")

    # If exists = false, if it exists, it will be overwritten.
    # index - False, dataframes index will not be written as a seperate column

    # Removed the unnamed 0 column from the dataframe
    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'], inplace=True)

    df.to_sql(table_name, database, if_exists='append', index=False)

    # Read the data from the database
    query = f"SELECT * FROM {table_name}"
    df_from_db = pd.read_sql_query(query, database)
    print(df_from_db.head())

    database.close()

    print("Successful creation of SQLite DB from Dataframe")


def sql_to_csv_postgres(connection_string, table_name, csv_file_path):

    # Define the connection and engine
    engine = create_engine('sqlite:///my_database.db')
    metadata = MetaData()

    # Define the table schema with a primary key on 'Cust_ID'
    ins_l_table = Table('ins_l', metadata,
                        Column('Cust_ID', String, primary_key=True),
                        Column('Date', String),
                        Column('Type', String),
                        Column('Reward_R', Integer),
                        Column('Reward_A', Integer),
                        Column('diff', Integer),
                        Column('Cov_Limit', Integer),
                        Column('Income', Integer),
                        Column('Cov_Income_Ratio', Float),
                        Column('fraud_flag', Integer)
                        )

    # Create the table in the database
    metadata.create_all(engine)

    # Load your data from CSV into a DataFrame
    df = pd.read_csv('ins_l.csv')

    # Optionally, drop any unwanted columns (e.g., an auto-generated index column)
    if 'ID' in df.columns:
        df.drop(columns=['ID'], inplace=True)

    # Insert the data into the pre-created table
    df.to_sql('ins_l', engine, if_exists='append', index=False)
