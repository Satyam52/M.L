# -*- coding: utf-8 -*-
"""
Created on Sun May 10 08:59:57 2020

@author: Mr. AKG
"""
# Multiple Linear Regression(Prequisite:Dummy Variable Trap---Naam to suna hi hoga,
#   P value)

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values


# Encoding categorical data
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3])], remainder='passthrough')
X = np.array(ct.fit_transform(X))


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

#This is the  testing of keyboard the if it workls but actuially its