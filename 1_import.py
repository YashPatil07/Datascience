# -*- coding: utf-8 -*-
"""1.import.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/195WDPts7v_zvdczZywReR4ff-jLr-Ybc
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn as sl

df=pd.read_csv('covid_19_clean_complete_2022.csv')
df.head()

df.isnull()

df.describe()

df.info()

df.shape

#change the datatype of data(object --> datatime)
df['Date']=pd.to_datetime(df['Date'])
df.info()
df['Country/Region']=df['Country/Region'].astype('string')
df.dtypes
