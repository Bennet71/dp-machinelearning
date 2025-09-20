import streamlit as st
import pandas as pd

st.title('Heart Disease Predictor')

st.info('This is a predictive AI application')

df = pd.read_csv(/kaggle/input/south-african-heart-disease-dataset/SAHeart.csv'')
df
