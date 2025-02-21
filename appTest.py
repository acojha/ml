# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 18:20:00 2025

@author: acojh
"""

import pandas as pd
#mport joblib
import pickle
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import RandomOverSampler
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score

framingham = pd.read_csv('framingham.csv')

# Dropping null values
framingham = framingham.dropna()
print(framingham.head())
print(framingham['TenYearCHD'].value_counts())

X = framingham.drop('TenYearCHD',axis=1)

y = framingham['TenYearCHD']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.20, random_state=42) 
oversample = RandomOverSampler(sampling_strategy='minority')
X_over, y_over = oversample.fit_resample(X_train,y_train)
rf_model = RandomForestClassifier()
rf_model.fit(X_over,y_over)

y_pred = rf_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Random Forest Model Accuracy: {accuracy * 100:.2f}%")

# save the classification model
#joblib.dump(rf_model, 'rf_model_pkl')
with open('rf_model_pkl', 'wb') as files:
    pickle.dump(rf_model, files)