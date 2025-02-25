# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 20:20:05 2025

@author: acojh
"""

import streamlit as st
import pickle
import pandas as pd

st.subheader("Quick Depression Assessment (Pfizer Inc's PHQ-9)")

st.html("<h3>Over the last TWO WEEKS, how often have you faced any of the following problems?</h3>")

col1, col2, col3 = st.columns(3)

# getting user input
phq1 = col1.selectbox("1.Little interest or pleasure in doing things",["Not at all", "Several days", "More than half the days", "Nearly every day"])
phq2 = col2.selectbox("2.Feeling down, depressed, or hopeless",["Not at all", "Several days", "More than half the days", "Nearly every day"])
phq3 = col3.selectbox("3.Trouble in sleeping or sleeping too much",["Not at all", "Several days", "More than half the days", "Nearly every day"])

phq4 = col1.selectbox("4.Feeling tired or having low energy",["Not at all", "Several days", "More than half the days", "Nearly every day"])
phq5 = col2.selectbox("5.Poor appetite or overeating",["Not at all", "Several days", "More than half the days", "Nearly every day"])
phq6 = col3.selectbox("6.Feeling failure, bad about yourself",["Not at all", "Several days", "More than half the days", "Nearly every day"])

phq7 = col1.selectbox("7.Trouble concentrating on things, reading, watching TV",["Not at all", "Several days", "More than half the days", "Nearly every day"])
phq8 = col2.selectbox("8.Moving or speaking slowly or being restless",["Not at all", "Several days", "More than half the days", "Nearly every day"])
phq9 = col3.selectbox("9.Thoughts of self-harm or suicide",["Not at all", "Several days", "More than half the days", "Nearly every day"])

btn=st.button('Predict', type="primary")
st.divider()
df_pred = pd.DataFrame([[phq1,phq2,phq3,phq4,phq5,phq6,phq7,phq8,phq9]],columns= ['phq1','phq2','phq3','phq4','phq5','phq6','phq7','phq8','phq9'])

def transform(data):
    result = 0
    if(data=='Several days'):
        result = 1
    elif(data=='More than half the days'):
        result = 2
    elif(data=='Nearly every day'):
        result = 3
    return(result)

df_pred['phq1'] = df_pred['phq1'].apply(transform)
df_pred['phq2'] = df_pred['phq2'].apply(transform)
df_pred['phq3'] = df_pred['phq3'].apply(transform)
df_pred['phq4'] = df_pred['phq4'].apply(transform)
df_pred['phq5'] = df_pred['phq5'].apply(transform)
df_pred['phq6'] = df_pred['phq6'].apply(transform)
df_pred['phq7'] = df_pred['phq7'].apply(transform)
df_pred['phq8'] = df_pred['phq8'].apply(transform)
df_pred['phq9'] = df_pred['phq9'].apply(transform)

# Load the saved model for prediction
with open('svm_model_pkl' , 'rb') as file:
    svm_model = pickle.load(file)

prediction = svm_model.predict(df_pred)
    
if btn:
  if(prediction[0]=='Normal'):
     st.write("Your are a NORMAL person")
  elif(prediction[0]=='Mild'):
     st.write("You have MILD depression! Be Watchful!")
  elif(prediction[0]=='Moderate'):
     st.write("You have MODERATE depression! Consider visiting a Doctor.")
  elif(prediction[0]=='High'):
     st.write("You have HIGH Depressive Disorder! Visit a doctor for Active Treatment!")
  elif(predictio[0]=='Severe'):
     st.write("You have SEVERE Depresive Disorder! You need IMMEDIATE Attention and Treatment!")


