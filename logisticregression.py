# -*- coding: utf-8 -*-
"""LogisticRegression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xrbedEHNXcCNX4YiFEycw6Vpr_JadNlQ
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import classification_report, confusion_matrix

# Load the dataset
data = pd.read_csv('Social_Network_Ads.csv')
data

data['Gender'] = pd.get_dummies(data['Gender'], drop_first=True)
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train the logistic regression model
classifier = LogisticRegression(random_state=0)
classifier.fit(X_train, y_train)

# Predict the test set results
y_pred = classifier.predict(X_test)
y_pred

print(classification_report(y_test,y_pred))

# Compute the confusion matrix
cm = confusion_matrix(y_test, y_pred)
print('Confusion matrix:')
print(cm)

# Compute the accuracy, error rate, precision, recall, and F1-score
accuracy = accuracy_score(y_test, y_pred)
error_rate = 1 - accuracy
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print('Accuracy: ', accuracy)
print('Error rate: ', error_rate)
print('Precision: ', precision)
print('Recall: ', recall)
print('F1-score: ', f1)

