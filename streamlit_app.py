import streamlit as st
import pandas as pd

st.title('Heart Disease Predictor')

st.info('This is a predictive AI application')

with st.expander("Data"):
  st.write('**Raw data**')
  df = pd.read_csv('SAHeart.csv')
  df.famhist = [1 if value == "Present" else 0 for value in df.famhist]
  df
  
  st.write('**X(Input variables)**')
  X = df.drop('chd', axis=1)
  X

  st.write('**Y(target variable)**')
  Y = df.chd
  Y

with st.expander("Data Visualization"):
  st.scatter_charts(data=df, x='age', y='tobacco', color='chd')

