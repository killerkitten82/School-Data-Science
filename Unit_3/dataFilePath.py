import os

dirname = os.path.join(os.path.dirname(__file__), "Data")

BTCFileName = "coin_BTC.csv"

BTCPath = os.path.join(dirname, BTCFileName)

def getFilePaths(unit):

    dirname = os.path.join(os.path.dirname(os.path.dirname(__file__)), unit, "More_Data")

    filePathDict = {}

    for file in os.listdir(dirname):
        filePathDict[file[:-4]] = os.path.join(dirname, file)

    return filePathDict
