import streamlit as st
import pandas as pd

st.title('Heart Disease Predictor')

st.info('INFS122 Semester project:predictive AI application')

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
  st.scatter_chart(data=df, x='age', y='tobacco', color='chd')

#User input
with st.sidebar:
    st.header("Patient health data")
    famhist = st.selectbox('**Family history**', ('Present', 'Absent'))
    sbp = st.slider('**Systolic blood pressure**', 100, 250, 175)
    tobacco = st.slider('**cumulative tobacco(kg)**', 0.0, 32.20, 16.1)
    idl = st.slider('**Colestorel level**', 0.98, 14.16, 7.57)
    adiposity = st.slider('**Severe overweight (numeric vector)**', 6.74, 42.17, 24.45 )
    
    

