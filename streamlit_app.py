import streamlit as st
import pandas as pd

st.title('Heart Disease Predictor')

st.info('INFS122 Semester project:predictive AI application')

with st.expander("Data"):
  st.write('**Raw data**')
  df = pd.read_csv('SAHeart.csv')
  df.chd = ['Positive' if value == 1 else 'Negative' for value in df.chd]
  df
  
  st.write('**X(Input variables)**')
  X_raw = df.drop('chd', axis=1)
  X_raw

  st.write('**Y(target variable)**')
  Y_raw = df.chd
  Y_raw

with st.expander("Data Visualization"):
  st.scatter_chart(data=df, x='age', y='tobacco', color='chd')

#User input
with st.sidebar:
    st.header("Patient health data")
    sbp = st.slider('**Systolic blood pressure**', 100, 250, 175)
    tobacco = st.slider('**cumulative tobacco(kg)**', 0.0, 32.20, 16.1)
    ldl = st.slider('**Colestorel level**', 0.98, 14.16, 7.57)
    adiposity = st.slider('**Severe overweight (numeric vector)**', 6.74, 42.17, 24.45 )
    famhist = st.selectbox('**Family history of heart disease**', ('Present', 'Absent'))
    typea = st.slider('**Type-A behaviour**', 13.00, 78.00, 45.50)
    obesity = st.slider('**Obesity**', 14.7, 46.58, 30.64)
    alcohol = st.slider('**Alcohol consumption**', 0.00, 147.19, 73.56)
    age = st.slider('**Age**', 18, 65, 42)

    #Creating a data frame for the input features.
    data = {'sbp': sbp,
            'tobacco': tobacco,
            'ldl': ldl,
            'adiposity': adiposity,
            'famhist': famhist,
            'typea': typea,
            'obesity': obesity,
            'alcohol': alcohol,
            'age': age}
    input_df = pd.DataFrame(data, index=[0])
    input_data = pd.concat([input_df, X_raw], axis=0)

with st.expander('input features'):
  st.write('**Input Features**')
  input_df
  st.write('**Combined patient data**')
  input_data
  
#Data Preparation
#encode x
encode = ['famhist']
df_patient = pd.get_dummies(input_data, prefix=encode)
df_patient[:1]

#Encode Y
target_mapper = {'Positive': 1,
                'Negative': 0}
def target_encode(val):
  return target_mapper[val]

y = Y_raw.apply(target_encode)
y

 
with st.expander('input features'):
  st.write('**Input Features**')
  input_df
  st.write('**Combined patient data**')
  input_data



  


    

