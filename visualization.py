#Start by importing
import streamlit as st
import numpy as np
import pandas as pd
import plotly as pt 
st.title('Lea Zaarour')
st.title('Streamlit Assignment') 

#title
st.title('Suicide rate')
#Design
col1, col2=st.columns([3,1])
with col1:
    st.markdown("This application is used to show the suicides rates in several countries and study which countries have the most suicide rates in order to implement an NGO to help people with suicide thoughts")
with col2:
    st.image('thumbs_b_c_aa3ee04afb9b4a1071bc0821fcb7cbb6.jpeg')
df= pd.read_csv('who_suicide_statistics.csv', sep= ':')
if 'number_of_rows' not in st.session_state or 'number_of_rows' not in st.session_state:
    st.session_state['number_of_rows']=5
    st.session_state['type']='Categorical'

increment= st.button('Show more columns')
if increment:
    st.session_state.number_of_rows += 5

decrement= st.button('Show fewer columns')
if decrement:
    st.session_state.number_of_rows -= 4

st.table(df.head(st.session_state['number_of_rows']))






