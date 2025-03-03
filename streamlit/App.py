import streamlit as st
import pandas as pd


def main():
    ''' Running the streamlit app '''

    st.title("Fraudalyze")

    col1, col2 = st.columns(2)
    col1.write(
        "- Welcome to Fraudalyze, a tool for detecting customer claims fraud. This is a project that is focused on using statistical and machine learning techniques on over 40000 datapoints of customer claims to visualize anamolies in the data and predict whether a claim is fraudulent or not.")
    col2.write("- We follow a pippeline approach to this project where we first explore the data, then preprocess the data, display anamolies, then train our model, and finally we deploy our model for you to use.")

    st.write("## What is this Dataset?")
    st.write("- This dataset contains over 40000 datapoints of customer claims.")

    # Read all the Rows of the Data

    st.write("##Ins_L File Containing Customer Insurance Profile")
    ins_l_data = pd.read_csv('../Fraud_Data/csv_data/ins_l.csv')
    st.write(ins_l_data)

    st.write("##transactions_ins File Containing Customer Insurance Profile")
    transactions_ins_data = pd.read_csv(
        "../Fraud_Data/csv_data/transactions_ins.csv")
    st.write(transactions_ins_data)


if __name__ == "__main__":
    main()

# streamlit run App.py
