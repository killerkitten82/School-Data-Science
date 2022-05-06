import pandas as pd

#total change from year to 2019
inflation2019Data = {
    2010: .1705, 
    2011: .1516,
    2012: .1163,
    2013: .0937,
    2014: .0779,
    2015: .0607,
    2016: .0594,
    2017: .0462,
    2018: .0244
}

def masterInflationFunction(df):
    return df.transform(inflation2019, axis=0)


def inflation2019(column):
    startYear = int(column.name[:4])
    return round(column * (1 + inflation2019Data[startYear]),2)