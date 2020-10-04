import quandl, math
import pandas
import numpy
import datetime


df = quandl.get("WIKI/AMZN")
print(df.tail())

print(df.head(2).round(1))
print("\n")

print(df.columns)
print(df.index)

df = df[('Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume')]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low'])/(df['Adj. Low']*100)
df['PCT_Change'] = (df['Adj. Close'] - df['Adj. Open'])/(df['Adj. Open']*100)

df = df[['Adj. Close', 'HCL_PCT', 'PCT_Change', 'Adj. Volume']]
print(df.head())
