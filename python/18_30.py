import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

bitcoin = pd.read_csv('BTC-EUR.csv', index_col='Date', parse_dates=True)
# bitcoin['Close'].plot(figsize=(9, 6))
# print(bitcoin.head())
# bitcoin.loc['2019-09', 'Close'].plot()
bitcoin.loc['2016':'2023', 'Close'].plot()
plt.show()
# print(bitcoin.index)
# if we need to change the time format use : pd.to_datetime('20129/03/20')
# timestamp('2019-03-20 00:00:00')

# using pandas in python swap two variables
def swap_variables(a, b):
    temp = pd.Series(a)
    a = pd.Series(b)
    b = pd.Series(temp)
    return a, b

