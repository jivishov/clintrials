import streamlit as st
import pandas as pd
from scipy.stats import ttest_rel

# Streamlit layout and logic
st.title("Paired t-test Calculator")

# Sidebar for future menu options
st.sidebar.title("Menu")
st.sidebar.text("Future options will go here.")

# Upload CSV file
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read and display data
    df = pd.read_csv(uploaded_file)
    st.write("Preview of uploaded data:")
    st.write(df.head())

    # Select columns
    selected_columns = st.multiselect("Select two columns for Paired t-test (Control and Treatment)", df.columns.tolist())

    if len(selected_columns) == 2:
        # Perform paired t-test
        col1_data = df[selected_columns[0]]
        col2_data = df[selected_columns[1]]

        t_stat, p_value = ttest_rel(col1_data, col2_data)

        # Display results
        st.write(f"t-statistic: **{t_stat:.4f}**")
        st.write(f"p-value: **{p_value:.4f}**")

        # Interpret p-value
        alpha = 0.05
        if p_value < alpha:
            st.write("The p-value is less than 0.05, which suggests that there is a statistically significant difference between the groups.")
        else:
            st.write("The p-value is greater than 0.05, indicating that there's not a statistically significant difference between the groups.")
