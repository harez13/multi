import streamlit as st
import pandas as pd
from datetime import timedelta, datetime

# Set page config
st.set_page_config(page_title="YouTube Channel Dashboard", layout="wide")

# Helper functions
@st.cache_data
def load_data():
    data = pd.read_excel("Data\Data Indeks Standar Pencemar Udara (ISPU) di Provinsi DKI Jakarta ).xls.xlsx")
    data['tanggal'] = pd.to_datetime(data['tanggal'])
    return data
