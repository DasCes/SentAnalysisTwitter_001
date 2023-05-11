import streamlit as st
import pandas as pd
import numpy as np
import plost
from PIL import Image
from datetime import datetime
import plotly.express as px

# Page setting
st.set_page_config(layout="wide", page_icon="Logo_of_Twitter.png",page_title="SenForWirn2023")

st.title("Sentiment analysis of last week", anchor=None, *, help=None)


with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Data
data = pd.read_csv('data/data.csv', index_col=[0])

data['created_at'] = pd.to_datetime(data['created_at'])
start_date = datetime.strptime("2023-03-10 01:44:38+00:00", "%Y-%m-%d %H:%M:%S%z")
end_date = datetime.strptime("2023-03-17 01:44:38+00:00", "%Y-%m-%d %H:%M:%S%z")
mask = (data['created_at'] > start_date) & (data['created_at'] <= end_date)
data = data.loc[mask]
data.reset_index(drop=True, inplace=True)

for i, x in enumerate(data.created_at):
    data.at[i, 'created_at'] = x.date().day

data["Sommatoria"] = 1




fig = px.bar(data, x='created_at', y='Sommatoria')
st.plotly_chart(fig, use_container_width=False, sharing="streamlit", theme="streamlit")



# Row B
b1, b2, b3, b4 = st.columns(4)
b1.metric("Temperature", "70 °F", "1.2 °F")
b2.metric("Wind", "9 mph", "-8%")
b3.metric("Humidity", "86%", "4%")
b4.metric("Humidity", "86%", "4%")

# # Row C
# c1, c2 = st.columns((7,3))
# with c1:
#     st.markdown('### Heatmap')
#     plost.time_hist(
#     data=data,
#     date='date',
#     x_unit='week',
#     y_unit='day',
#     color='temp_max',
#     aggregate='median',
#     legend=None)
# with c2:
#     st.markdown('### Bar chart')
#     plost.donut_chart(
#         # data=stocks,
#         theta='q2',
#         color='company')