import streamlit as st
import pandas as pd

st.title('Heart Disease Predictor')

st.info('INFS122 Semester project:predictive AI application')

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

with st.expander("Data Visualization"):
  st.scatter_chart(data=df, x='age', y='tobacco', color='chd')

#User input
with st.sidebar:
    st.header("Patient health data")
    sbp = st.slider('**Systolic blood pressure**', 100, 250, 175)
    tobacco = st.slider('**cumulative tobacco(kg)**', 0.0, 32.20, 16.1)
    idl = st.slider('**Colestorel level**', 0.98, 14.16, 7.57)
    adiposity = st.slider('**Severe overweight (numeric vector)**', 6.74, 42.17, 24.45 )
    famhist = st.selectbox('**Family history of heart disease**', ('Present', 'Absent'))
    typea = st.slider('**Type-A behaviour**', 13.00, 78.00, 45.50)
    Obesity = st.slider('**Obesity**', 14.7, 46.58, 30.64)
    alcohol = st.slider('**Alcohol consumption**', 0.00, 147.19, 73.56)
    age = st.slider('**Age**', 18, 65, 42)

    #Creating a data frame for the input features.
    data = {'Systolic blood pressure': sbp,
            'cumulative tobacco(kg)': tobacco,
            'Colestorel level': idl,
            'Severe overweight (numeric vector)': adiposity,
            'famhist': famhist,
            'Type-A behaviour': typea,
            'Obesity': Obesity,
            'Alcohol consumption': alcohol,
            'Age': age}
    input_df = pd.DataFrame(data, index=[0])
    input_data = pd.concat([input_df, X], axis=0)

with st.expander('input features'):
  st.write('**Input Features**')
  input_df
  st.write('**Combined patient data**')
  input_data

#encode
encode = ['famhist']
df_patient = pd.get_dummies(input_data, prefix=encode)
df_patient[:1]

  


    

