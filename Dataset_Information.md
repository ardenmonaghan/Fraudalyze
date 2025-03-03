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

## Pipeline 

1. Load data into Pandas Dataframes and SQL Database

2. Perform data cleaning for ins_l or ins_feat and standardize formats for inconsistent data
- (Definition: Refining your dataset by correcting or removing erroneous data.
Using SQL: Replacing NULL values  and Standardizing format)

3. Feature Engineering: Creating new variables from raw data that help improve the models performance 
- eg: Cov_Income_Ratio (Ratio of Cov_Limit and Income)

4. Exploratory Data Analysis (EDA) & Visualization 
- Process of summarizing the main characteristics of the datasets, providing statistics and key visualizations 
- Descriptive Statistics (Calculating Averages, Medians, Variances)
- Correlations (Determining Relationships between features)
- Data Visualization (Graphically representing data using histograms scatterplots and boxplots to identify trends (Can be done with matplotlib and streamlit))

5. Anamoly Detecttion using kNN or Isolation Forest 
- Integrated by first Data Cleaning and Data engeineering 
- Exploring it into python and using sklearn. 
- This can be inputted for fraud detection model.

5. Supervised Learning Model Deployment:
- Feature selection
- Train test split
- Model training (using a model like Logistic Regression or Random Forest)



