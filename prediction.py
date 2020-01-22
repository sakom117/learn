import quandl
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
df = quandl.get("WIKI/fb")
print(df.head())

df = df[['Adj.Close']]
print(df.head())
