# -*- coding: utf-8 -*-
"""8data_vistualization.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cyNDHUOKiXNbybiwKlU5e_pFKN5quqHs
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('Titanic-Dataset.csv')

df.head()

sns.barplot(x='Sex',y='Age',data=df)

sns.catplot(x='Sex',hue='Survived',kind='count',data=df)

sns.histplot(x='Fare',binwidth=30,data=df)

sns.lineplot(x='Sex',y='Age',data=df)

