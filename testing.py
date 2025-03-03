from Analysis_Scripts.csv_to_sql import csv_to_sql

TABLE_INS = '''
     CREATE TABLE IF NOT EXISTS ins_l (
         Cust_ID TEXT PRIMARY KEY,
         Date TEXT,
         Type TEXT,
         Reward_R INTEGER,
         Reward_A INTEGER,
         diff INTEGER,
         Cov_Limit INTEGER,
         Income INTEGER,
         Cov_Income_Ratio REAL,
         fraud_flag INTEGER
     )
 '''

TABLE_TRANSACTIONS = '''
    
     CREATE TABLE IF NOT EXISTS transactions_ins (
         Transaction_ID INTEGER PRIMARY KEY AUTOINCREMENT,
         Cust_ID INTEGER,
         Date TEXT,
         Transaction_Type TEXT,
         TYPE TEXT,
         Reward_R INTEGER,
         Reward_A INTEGER,
         diff INTEGER,
         Cov_Limit INTEGER,
         Income INTEGER
     )
 '''


if __name__ == "__main__":
    # csv_to_sql('Fraud_Data/csv_data/ins_l.csv',
    #            'Fraud_Data/sql_data/ins_l.db',
    #            'ins_l', TABLE_INS)

    # Putting the transactions into the same table
    csv_to_sql('Fraud_Data/csv_data/transactions_ins.csv',
               'Fraud_Data/sql_data/ins_l.db',
               'transactions_ins', TABLE_TRANSACTIONS)
