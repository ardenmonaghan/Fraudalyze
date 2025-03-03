import streamlit as st
import pandas as pd


def main():
    ''' Running the streamlit app '''

    st.title("Fraudalyze")

    col1, col2 = st.columns(2)
    col1.write(
        "Welcome to Fraudalyze, a tool for detecting customer claims fraud. This is a project that is focused on using statistical and machine learning techniques on over 40000 datapoints of customer claimms")

    # Read all the Rows of the Data
    data = pd.read_csv('../Fraud_Data/csv_data/ins_l.csv')
    st.write(data)


if __name__ == "__main__":
    main()

# streamlit run App.py
