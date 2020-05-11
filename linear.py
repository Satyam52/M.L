# -*- coding: utf-8 -*-
"""
Created on Mon May 11 18:16:59 2020

@author: Mr. AKG
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Train_dataset = pd.read_csv('train.csv')
Test_dataset = pd.read_csv('test.csv')

X_train = Train_dataset.iloc[:,:-1].values
y_train = Train_dataset.iloc[:,1].values
X_test = Test_dataset.iloc[:,:-1].values
y_test = Test_dataset.iloc[:,1].values

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)

y_pred = regressor.predict(X_test)
accuracy = regressor.score(X_test,y_test)*100
print(accuracy,"%")
# Plotto\ing
plt.scatter(X_test,y_test,color="red")
plt.scatter(X_train,y_train,color="grey")
plt.plot(X_test,y_pred,color="blue")
plt.show()