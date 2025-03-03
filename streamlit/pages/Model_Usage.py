import streamlit as st
import pandas as pd
import plotly.graph_objects as go


def donut_chart_visualization(percentage):
    # Create a simple donut chart showing only the percentage
    fig = go.Figure(go.Pie(
        values=[percentage, 100-percentage],
        hole=0.7,
        # Blue for filled, light gray for empty
        marker_colors=['#1f77b4', '#e0e0e0'],
        showlegend=False,
        textinfo='none',  # Hide default text
    ))

    # Add the percentage text in the center
    fig.add_annotation(
        text=f"{percentage}%",
        font=dict(size=30, family="Arial", color="black"),
        showarrow=False,
        x=0.5,
        y=0.5
    )

    # Clean up the layout
    fig.update_layout(
        width=300,
        height=300,
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor='rgba(0,0,0,0)'
    )

    return fig


def model_usage():
    st.title("Model Usage")

    st.write("This is a page for the model usage. Here we can test our Regression Model on determining whether a specific claim is fraudulent.")
    st.write(
        "You will be able to input the variables below and see the prediction score for the claim")

    st.write("## Input Information")

    col3, col4 = st.columns(2)
    st.write("## Input Data")
    col3, col4 = st.columns(2)
    customer_id = col3.text_input("Customer_ID")
    date = col3.text_input("Date")
    type = col3.text_input("Type")
    reward_r = col3.text_input("Reward_R")
    reward_a = col4.text_input("Reward_A")
    diff = col4.text_input("diff")
    cov_limit = col4.text_input("Cov_Limit")
    income = col4.text_input("Income")

    #############################################
    # Predict the Score using Our Model Here
    #############################################

    percentage = 75

    fig = donut_chart_visualization(percentage)

    st.plotly_chart(fig)


# Display in Streamlit
model_usage()
