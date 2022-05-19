import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import norm

from dataFilePath import *

path = getFilePaths("Unit_3")

BTCData = pd.read_csv(path["coin_BTC"])
BTCData.set_index(BTCData["Date"], inplace = True)
BTCData.drop(columns=["Date"], inplace = True)
BTCData.index = pd.to_datetime(BTCData.index)
