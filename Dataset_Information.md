# Dataset Information

## ins_l.csv

Content: Aggregated, customer-level data.

- Cust_ID: Customer identifier. (Unique)

- Date: The date associated with the record.

- Type: Likely denotes the type of transaction or policy (e.g., T, V, W). Analyze whether certain types have higher fraud rates or patterns in other metrics

- Reward_R & Reward_A: Reward-related values.

- diff: A derived difference metric (possibly between rewards or other measures).

- Cov_Limit & Income: Coverage limit and income details. (The insurance product is proportionate to the customers financial status)

- Cov_Income_Ratio: Ratio between coverage limit and income. (Derived ratio of the coverage limit to the customer's income) (High or low ratios may be red flags)

- fraud_flag: Indicates whether the record is flagged as fraud (0 means not fraud, and 1 would typically indicate fraud).

### Important Terminology.



