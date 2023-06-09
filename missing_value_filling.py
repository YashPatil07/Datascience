# -*- coding: utf-8 -*-
"""missing_value_filling.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16TP7hhlGqQhDVQ5q2rRyGVggclYx50Bj
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('Academic-Performance-Dataset.csv')
df.head()
df.shape
df.info()

#Handiling the missing value
df.isnull().sum()

#make a list of column having missing values
#create col with 'na' column
missing_value=[]
for col in df.columns:
  if df[col].isna().any():
    missing_value.append(col)

missing_value

#fill the missing value using mean for flot and int datatypes and for other forward fill
for col in missing_value:
  col_dt=df[col].dtypes
  if(col_dt=='int64' or col_dt=='float64'):
    outliers=(df[col]<0)|(100<df[col])
    df.loc[outliers,col]=np.nan
    df[col]=df[col].fillna(df[col].mean())
  else:
     df[col]=df[col].fillna(method='ffill')

df

#correction in total marks,percentage after filling missing value
df['Total Marks']=df['Phy_marks']+df['Che_marks']+df['EM1_marks']+df['PPS_marks']+df['SME_marks']
df['Percentage']=df['Total Marks']/5
df

#outlier detection
import matplotlib.pyplot as plt
plt.figure(figsize=(4,4))
df_list = ['Attendence', 'Phy_marks', 'Che_marks', 'EM1_marks', 'PPS_marks', 'SME_marks']
fig, axes = plt.subplots(2, 3)
fig.set_dpi(120)

count=0
for r in range(2):
    for c in range(3):
        _ = df[df_list[count]].plot(kind = 'box', ax=axes[r,c])
        count+=1

#removal of outlier from che_marks
Q1 = df['Che_marks'].quantile(0.25)
Q3 = df['Che_marks'].quantile(0.75)
IQR = Q3 - Q1

Lower_limit = Q1 - 1.5 * IQR
Upper_limit = Q3 + 1.5 * IQR

print(f'Q1 = {Q1}, Q3 = {Q3}, IQR = {IQR}, Lower_limit = {Lower_limit}, Upper_limit = {Upper_limit}')

df[(df['Che_marks'] < Lower_limit) | (df['Che_marks'] > Upper_limit)]

#convert in to normal distribution
#Binning using frequeny
def BinningFunction(column, cut_points, labels = None) :
    break_points=[column.min()] + cut_points + [column.max( )]
    print('Gradding According to percentage \n>60 = F \n60-70 = B \n70-80 = A\n80-100 = O')
    return pd.cut(column, bins=break_points, labels=labels, include_lowest=True)

cut_points=[60, 70, 80]
labels=['F', 'B', 'A', 'O']
df['Grade']=BinningFunction(df['Percentage'], cut_points, labels)

df

