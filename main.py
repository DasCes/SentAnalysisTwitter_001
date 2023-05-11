import streamlit as st
import pandas as pd
import numpy as np
import plost
from PIL import Image

# Page setting
st.set_page_config(layout="wide", page_icon="Logo_of_Twitter.png",page_title="senForWirn2023")


with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Data
data = pd.read_csv('data/dataset_from_06_03_to_02_04.csv')
stocks = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/stocks_toy.csv')

# Row A
a1, a2, a3 = st.columns(3)
a1.image(Image.open('Logo_of_Twitter.png'))
a2.metric("Wind", data['text'].iloc[0], "-8%")
a3.metric("Humidity", "86%", "4%")


# Row B
b1, b2, b3, b4 = st.columns(4)
b1.metric("Temperature", "70 °F", "1.2 °F")
b2.metric("Wind", "9 mph", "-8%")
b3.metric("Humidity", "86%", "4%")
b4.metric("Humidity", "86%", "4%")

# Row C
c1, c2 = st.columns((7,3))
with c1:
    st.markdown('### Heatmap')
    plost.time_hist(
    data=data,
    date='date',
    x_unit='week',
    y_unit='day',
    color='temp_max',
    aggregate='median',
    legend=None)
with c2:
    st.markdown('### Bar chart')
    plost.donut_chart(
        data=stocks,
        theta='q2',
        color='company')