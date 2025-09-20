import streamlit as st
import pandas as pd

st.title('Heart Disease Predictor')

st.info('This is a predictive AI application')

with st.expander("Data"):
  st.write('**Raw data**')
  df = pd.read_csv('SAHeart.csv')
  df
  
  st.write('**X(Input variables)**')
  X = df.drop('chd', axis=1)
  X

  st.write('**Y(target variable)**')
  Y = df.chd
  Y

