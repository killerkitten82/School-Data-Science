import pandas as pd
import matplotlib.pyplot as plt
import math

from dataFilePath import *

pd.set_option("display.max_columns", None)

# --------------------IMPORT DATA FROM CSV-------------------- #

# BTC
BTCData = pd.read_csv(BTCPath)
BTCData.set_index(BTCData["Date"], inplace = True)
BTCData.drop(columns=["Date"], inplace = True)
# BTCData.sort_index(inplace=True)

BTCData.index = pd.to_datetime(BTCData.index)


BTCData.plot.line()

plt.show()
