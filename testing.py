from Analysis_Scripts.csv_to_sql import csv_to_sql

if __name__ == "__main__":
    csv_to_sql('Fraud_Data/csv_data/ins_l.csv',
               'Fraud_Data/sql_data/ins_l.db',
               'ins_l')
