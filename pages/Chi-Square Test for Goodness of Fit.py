import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import chisquare

# Streamlit layout and logic
st.title("Chi-Square Test for Goodness of Fit Calculator")

# # Sidebar for future menu options
# st.sidebar.title("Menu")
# st.sidebar.text("Future options will go here.")

# Upload CSV file
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read and display data
    df = pd.read_csv(uploaded_file)
    st.write("Preview of uploaded data:")
    st.write(df.head())

    # EDA: Bar plot for Observed and Expected data
    st.write("### Exploratory Data Analysis")
    st.write("Bar plot for Observed and Expected data:")
    fig, ax = plt.subplots()
    df.plot(kind='bar', ax=ax)
    plt.xlabel('Categories')
    plt.ylabel('Frequency')
    plt.title('Observed vs Expected')
    st.pyplot(fig)

    # Select columns
    observed_column = st.selectbox("Select the column for Observed data", df.columns.tolist())
    expected_column = st.selectbox("Select the column for Expected data", df.columns.tolist())

    if observed_column and expected_column:
        # Perform Chi-Square Test for Goodness of Fit
        observed_data = df[observed_column]
        expected_data = df[expected_column]
        
        chi2_stat, p_value = chisquare(f_obs=observed_data, f_exp=expected_data)

        # Display results
        st.write(f"Chi-Square statistic: **{chi2_stat:.4f}**")
        st.write(f"p-value: **{p_value:.4f}**")

        # Interpret p-value
        alpha = 0.05
        if p_value < alpha:
            st.write("The p-value is less than 0.05, suggesting that the observed distribution is significantly different from the expected distribution.")
        else:
            st.write("The p-value is greater than 0.05, indicating that the observed distribution is not significantly different from the expected distribution.")
