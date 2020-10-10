import quandl, math
import pandas as pd
import numpy as np
import datetime

from sklearn.linear_model import LinearRegression
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split


df = quandl.get("WIKI/AMZN")


df = df[['Adj. Close']]

forecast_out = int(30)
df['Prediction'] = df[['Adj. Close']].shift(-forecast_out)

print(df.tail())

x = np.array(df.drop(['Prediction'], 1))
x = preprocessing.scale(x)

x_forecast = x[-forecast_out:]
x = x[:-forecast_out]

y = np.array(df['Prediction'])
y = y[:-forecast_out]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

clf = LinearRegression()
clf.fit(x_train, y_train)

confidence = clf.score(x_test, y_test)
print("Confidence: ", confidence)

forecast_prediction = clf.predict(x_forecast)
print(forecast_prediction)

