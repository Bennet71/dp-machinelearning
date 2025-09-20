import streamlit as st
import pandas as pd

st.title('Heart Disease Predictor')

st.info('This is a predictive AI application')

df = pd.read_csv("https://www.kaggle.com/code/betismeddhia/heart-disease-prediction-with-linear-regression.csv")
df
