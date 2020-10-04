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
