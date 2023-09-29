import numpy as np
import pandas as pd
import streamlit as st
#from pandas_profiling import ProfileReport
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Web App Title
st.markdown('''
# **Exploratory data analysis/Kəşfiyyatçı Data Təhlili**
''')

# Upload CSV data
st.header('1. Upload your CSV data/Verilənləri CSV formatında  yükləyin')
uploaded_file = st.file_uploader("Upload your input CSV file/CSV formatında faylı yükləyin", type=["csv"])
st.markdown("""
[Example CSV input file](https://raw.githubusercontent.com/jivishov/clintrials/main/sample_datasets/cancer_dataset.csv)
""")

# Pandas Profiling Report
if uploaded_file is not None:
    @st.cache_data
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True,plot={"dpi": 500, "image_format": "png"})
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Verilənlərin Profil Təhlili Hesabatı**')
    st_profile_report(pr)
else:
    st.info('Awaiting for CSV file to be uploaded/CSV faylın yükləyinməsini gözləyir...')
    url=""
    choice=st.radio("Choose sample dataset to load/Nümünə verilənləri yükləmək üçün seçin",
                    ["European Drug Development","USA Cancer Statistics, 1999-2020 Mortality Incidence Rate Ratios Results"])
    if choice=="European Drug Development":
        url="https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2023/2023-03-14/drugs.csv"
    else:
        url="https://raw.githubusercontent.com/jivishov/clintrials/main/sample_datasets/cancer_dataset.csv"
    if st.button('Press to use Example Dataset/Nümunə verilənləri işlət'):
        # Example data        
        @st.cache_data     
        def load_data():
            # url="https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2023/2023-03-14/drugs.csv"
            a=pd.read_csv(url)
            
            # a = pd.DataFrame(
            #     np.random.rand(100, 5),
            #     columns=['a', 'b', 'c', 'd', 'e']
            # )
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True,plot={"dpi": 500, "image_format": "png"})
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Data Profiling Report/Verilənlərin Profil Təhlili Hesabatı**')
        st_profile_report(pr)