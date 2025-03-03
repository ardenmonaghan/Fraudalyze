# Fraudalyze

Fraudalyze is a Data Analytics project that Uses Both Machine Learning and Statistical Methodologies to detect Fraud Cases on a test dataset Customer Insurance Claims with other 40000 Users and 200000 Logged Claims for data points. Anamolies are detected and visualized onto streamlit.A Machine Learning model is also developed which takes in a set of customer information and predicts the probability of that case being a fraud case. 

## Dataset Information:

There are two major datasets operated on. 

customer_info.csv: This dataset contains information about the customers such as their income, coverage limit, and other relevant information.
transactions.csv: Contains information about transactions that have happened with a current user and their income, coverage limit, and Reward information for their account.

## Directory Structure:

├── README.md                  # Project overview and documentation
├── Dataset_Information.md    # Important Dataset and Pipeline Information
├── Analysis_Scripts          # Scripts used for Data Analysis and Feature Engineering. 
├── Streamlit_App             # Streamlit App for Data Visualization and Anomaly Detection that Users can interact with. 
├── Model_Training            # Directory for all the scripts used to train the model predicting fraud claims. 
├── Fraud_Data                # All the datasets both in csv and SQL. 

### Technical Stack
- Python 3.10
- SQLite

### Libraries Used
- Scikit Learn
- Pandas
- Streamlit
- Matplotlib
- Numpy

## Requirements







