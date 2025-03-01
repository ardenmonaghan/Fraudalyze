import pandas as pd
import sqlite3


def csv_to_sql(csv_file, connection_string):
    ''' Read a pandas dataframe from a csv file and insert it into a sql table.'''

    df = pd.read_csv(csv_file)

    database = sqlite3.connect(connection_string)

    # If exists = false, if it exists, it will be overwritten.
    # index - False, dataframes index will not be written as a seperate column
    df.to_sql('ins_feat_table', database, if_exists='replace', index=False)

    df_from_db = pd.read_sql_query('SELECT * FROM ins_feat_table', database)
    print(df_from_db.head())

    database.close()

    print("Successful creation of SQLite DB from Dataframe")

