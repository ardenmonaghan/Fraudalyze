# Fraudalyze

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





