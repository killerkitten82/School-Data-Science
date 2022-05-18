from importlib.resources import path
from operator import index
import pandas as pd
import matplotlib.pyplot as plt
import math

from dataFilePath import *

pd.set_option("display.max_columns", None)

# --------------------IMPORT DATA FROM CSV-------------------- #

paths = getFilePaths("Unit_3")

# print(paths)

coins = {}

for coin in paths:
    coins[coin] = pd.read_csv(paths[coin])
    coins[coin].set_index(coins[coin]["Date"], inplace = True)
    coins[coin].drop(columns=["Date"], inplace = True)

    coins[coin].index = pd.to_datetime(coins[coin].index)

# print(coins)

max_min = {}

for coin in coins:
    max_min[coin] = [coins[coin].loc[:, "High"].max(), coins[coin].loc[:, "Low"].min() ]

print(max_min)
maxDF = pd.DataFrame(max_min,index=["Max", "Min"])

print(maxDF)

# maxDF.drop(columns=["coin_WrappedBitcoin", "coin_Bitcoin"]).transpose().plot.pie(y="Max", legend=None, autopct="%1.1f%%")

maxDF.drop(columns=["coin_WrappedBitcoin", "coin_Bitcoin"]).transpose().plot.bar(y="Max", legend=None)



# plt.legend(loc="None")

plt.show()



