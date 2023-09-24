import streamlit as st
import pandas as pd
from scipy.stats import kruskal

# Streamlit layout and logic
st.title("Kruskal-Wallis H Test Calculator")

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
    selected_columns = st.multiselect("Select columns for Kruskal-Wallis H Test", df.columns.tolist())

    if len(selected_columns) >= 2:
        # Perform Kruskal-Wallis H Test
        selected_data = [df[col] for col in selected_columns]
        h_stat, p_value = kruskal(*selected_data)

        # Display results
        st.write(f"H-statistic: **{h_stat:.4f}**")
        st.write(f"p-value: **{p_value:.4f}**")

        # Interpret p-value
        alpha = 0.05
        if p_value < alpha:
            st.write("The p-value is less than 0.05, suggesting that there is a statistically significant difference between the groups.")
        else:
            st.write("The p-value is greater than 0.05, indicating that there's not a statistically significant difference between the groups.")
