# -*- coding: utf-8 -*-
"""HomeRatePrediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hyQbYNfbRW0CBNy8wYfN1ncTVPVSEgxv

Create a Linear Regression Model using Python/R to **predict home prices**	using	Boston	Housing	Dataset (https://www.kaggle.com/c/boston-housing).

 The Boston Housing dataset contains information about various houses in Boston through different parameters. There are 506 samplesand 14 feature variables in this dataset.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('boston.csv')
df.head()

df.plot.scatter('RM', 'MEDV', figsize=(6, 6));

"""In this plot its clearly to see a linear pattern. Wheter more average number of rooms per dwelling, more expensive the median value is."""

plt.subplots(figsize=(10,8))
sns.heatmap(df.corr(), cmap = 'magma', annot = True, fmt = '.1f');

"""At this heatmap plot, we can do our analysis better than the pairplot.

Lets focus at the last line, where y = MEDV:

When shades of Blue: the more Blue color is on X axis, smaller the MEDV. Negative correlation                           
When light colors: those variables at axis x and y, they dont have any relation. Zero correlation                               
When shades of Red : the more Red color is on X axis, higher the MEDV. Positive correlation

# Trainning Linear Regression Model
**Define X and Y**

X: Varibles named as predictors, independent variables, features.                                                               
Y: Variable named as response or dependent variable
"""

X = df[df.columns[:-1]]
Y = df['MEDV']

"""**Import sklearn librarys:**    
train_test_split, to split our data in two DF, one for build a model and other to validate.                                     
LinearRegression, to apply the linear regression.
"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

# Split DataSet
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)
sc_X = StandardScaler()
X_train_ = sc_X.fit_transform(X_train)
X_test_ = sc_X.transform(X_test)

print(f'Train Dataset Size - X: {X_train.shape}, Y: {Y_train.shape}')
print(f'Test  Dataset Size - X: {X_test.shape}, Y: {Y_test.shape}')

# Model Building
lm = LinearRegression()
lm.fit(X_train_, Y_train)
predictions = lm.predict(X_test_)

# Model Visualization
plt.figure(figsize=(6, 6));
plt.scatter(Y_test, predictions);
plt.xlabel('Y Test');
plt.ylabel('Predicted Y');
plt.title('Test vs Prediction');

plt.figure(figsize=(6, 6));
sns.regplot(x = X_test['RM'], y = predictions, scatter_kws={'s':5});
plt.scatter(X_test['RM'], Y_test, marker = '+');
plt.xlabel('Average number of rooms per dwelling');
plt.ylabel('Median value of owner-occupied homes');
plt.title('Regression Line Tracing');

from sklearn import metrics

print('Mean Absolute Error:', metrics.mean_absolute_error(Y_test, predictions))
print('Mean Square Error:', metrics.mean_squared_error(Y_test, predictions))
print('Root Mean Square Error:', np.sqrt(metrics.mean_squared_error(Y_test, predictions)))

# Model Coefficients
coefficients = pd.DataFrame(lm.coef_.round(2), X.columns)
coefficients.columns = ['Coefficients']
coefficients

"""How to interpret those coefficients:
    they are in function of MEDV, so 
    
    for one unit that NOX increase, the house value decrease 'NOX'*1000 (Negative correlation) money unit.
    for one unit that RM increase, the house value increase 'RM'*1000 (Positive correlation) money unit.

*1000 because the MEDV is in 1000
and this apply to the other variables/coefficients.
    
"""

