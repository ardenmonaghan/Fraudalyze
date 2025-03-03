SELECT * FROM ins_l
WHERE Cov_Limit > 30000;

SELECT * FROM ins_l
WHERE fraud_flag = 1;


DROP TABLE IF EXISTS transactions_ins;