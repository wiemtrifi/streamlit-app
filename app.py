import streamlit as st
import pandas as pd
import numpy as np


data_url=(
"/home/rhyme/desktop/project/Motor_Vehicle_Collisions_-_Crashes"
)

st.title("motor vehicule collisions in New York City")
st.markdown("this application is streamlit dashboard to analyze motor vehicule collisions in NYC 💥")

#st.title("hello world ")
#st.markdown("### my first streamlit dashbord")
def load_data(nrows):
    data=pd.read_csv(data_url,nrows=nrows,parse_dates=[['crash_date','crash_time']])
    data.dropna(subset=['latitude','longitude'],inplace=True)
    lowercase= lambda x : str(x).lower()
    data.rename(lowercase,)
