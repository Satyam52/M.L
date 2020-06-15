# -*- coding: utf-8 -*-
"""
Created on Sat May  9 20:52:12 2020

@author: Mr. AKG
"""
# Simple Linear Regression

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Fitting into linear regression model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train) #successfully fitted or trained model

# Predict Test set results
y_pred = regressor.predict(X_test)

# Visualizing the Training Set results
plt.scatter(X_train,y_train,color="red")
plt.plot(X_train,regressor.predict(X_train),color="blue")
plt.title("Salary vs Experience(Training Set)")
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.show()

# Visualise the Test Set results
plt.scatter(X_test,y_test,color="red")
plt.plot(X_test,y_pred,color="blue")
plt.title("Salary vs Experience (Test Set)")
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.show()
