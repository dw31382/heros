#!/usr/bin/env python3

import pandas as pd
import random
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

# read csv file
df = pd.read_csv("log.csv")

X = df[['cpu', 'freq', 'fan', 'load']]
y = df['temp']

# scale data
X = scale.fit_transform(X)
y = scale.fit_transform(y.values.reshape(-1, 1))

# find correlation between features and target
print(df.corr())

# plot correlation between features and target
plt.matshow(df.corr())
plt.xticks(range(len(df.columns)), df.columns)
plt.yticks(range(len(df.columns)), df.columns)
plt.colorbar()
plt.show()