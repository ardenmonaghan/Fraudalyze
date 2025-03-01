# Fraudalyze

ins_l.csv
Content: Aggregated, customer-level data.
Key Columns:
- Cust_ID: Customer identifier.
- Date: The date associated with the record.
- Type: Likely denotes the type of transaction or policy (e.g., T, V, W).
- Reward_R & Reward_A: Reward-related values.
- diff: A derived difference metric (possibly between rewards or other measures).
- Cov_Limit & Income: Coverage limit and income details.
- Cov_Income_Ratio: Ratio between coverage limit and income.
- fraud_flag: Indicates whether the record is flagged as fraud (0 means not fraud, and 1 would typically indicate fraud).