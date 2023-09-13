import streamlit as st
import pandas as pd
from scipy.stats import chi2_contingency

# Streamlit layout and logic
st.title("Chi-Square Test for Independence Calculator")

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

    # Select columns
    selected_columns = st.multiselect("Select two columns for Chi-Square Test", df.columns.tolist())

    if len(selected_columns) == 2:
        # Create a contingency table
        contingency_table = pd.crosstab(df[selected_columns[0]], df[selected_columns[1]])

        # Perform Chi-Square Test
        chi2, p_value, dof, expected = chi2_contingency(contingency_table)

        # Display results
        st.write(f"Chi-Square statistic: **{chi2:.4f}**")
        st.write(f"p-value: **{p_value:.4f}**")
        st.write(f"Degrees of Freedom: **{dof}**")

        # Interpret Chi-Square statistic and DoF
        st.write("### Interpretation:")
        st.write(f"- **Chi-Square Statistic**: A higher value suggests that the observed distribution is significantly different from the expected distribution under the null hypothesis of independence.")
        st.write(f"- **Degrees of Freedom**: This is calculated as \((\ text{{Number of rows}} - 1) \ times (\ text{{Number of columns}} - 1)\) in the contingency table. It's important for determining the critical value of the Chi-Square distribution.")

        # Interpret p-value
        alpha = 0.05
        if p_value < alpha:
            st.write("The p-value is less than 0.05, suggesting that the variables are not independent.")
        else:
            st.write("The p-value is greater than 0.05, indicating that the variables are independent.")
