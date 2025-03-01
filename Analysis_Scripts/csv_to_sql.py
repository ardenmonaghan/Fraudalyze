import pandas as pd
import sqlite3


def csv_to_sql(csv_file_path, connection_string):
    ''' Read a pandas dataframe from a csv file and insert it into a sql table.'''

    print(f"Reading csv file from {csv_file_path}")
    df = pd.read_csv(csv_file_path)

    database = sqlite3.connect(connection_string)
    print(f"Connected to database {connection_string}")

    # If exists = false, if it exists, it will be overwritten.
    # index - False, dataframes index will not be written as a seperate column
    df.to_sql('ins_feat_table', database, if_exists='replace', index=False)

    df_from_db = pd.read_sql_query('SELECT * FROM ins_l', database)
    print(df_from_db.head())

    database.close()

    print("Successful creation of SQLite DB from Dataframe")
