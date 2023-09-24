import streamlit as st
import pandas as pd
from scipy.stats import ttest_ind

# Streamlit layout and logic
st.title("Independent t-test Calculator")

# # Sidebar for future menu options
# st.sidebar.title("Menu")
# st.sidebar.text("Future options will go here.")

st.markdown('<a href="https://drive.google.com/drive/folders/1Fo3vRuh0MMHw8iHipQk8jaWnEiErRZ8L?usp=drive_link" target="_blank">Download sample datasets/Nümunə verilənləri endirin</a>', unsafe_allow_html=True)

# Upload CSV file
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read and display data
    df = pd.read_csv(uploaded_file)
    st.write("Preview of uploaded data:")
    st.write(df.head())

    # Select columns
    selected_columns = st.multiselect("Select two columns for Independent t-test", df.columns.tolist())

    if len(selected_columns) == 2:
        # Perform Independent t-test
        col1_data = df[selected_columns[0]]
        col2_data = df[selected_columns[1]]

        t_stat, p_value = ttest_ind(col1_data, col2_data)

        # Display results
        st.write(f"t-statistic: **{t_stat:.4f}**")
        st.write(f"p-value: **{p_value:.4f}**")

        # Interpret p-value
        alpha = 0.05
        if p_value < alpha:
            st.write("The p-value is less than 0.05, suggesting that there is a statistically significant difference between the groups.")
        else:
            st.write("The p-value is greater than 0.05, indicating that there's not a statistically significant difference between the groups.")
