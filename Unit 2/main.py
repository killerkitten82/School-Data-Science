import pandas as pd
import matplotlib.pyplot as plt
import math

from inflationFunction import *
from dataFilePath import salaryPath, graduationPath, ratioPath, minimumPath

pd.set_option("display.max_columns", None)

# --------------------IMPORT DATA FROM CSV-------------------- #

# salary data
salaryData = pd.read_csv(salaryPath)
salaryData.set_index(salaryData["State"], inplace = True)
salaryData.drop(columns=["State"], inplace = True)

# graduation data
graduationData = pd.read_csv(graduationPath)
graduationData.set_index(graduationData["State"], inplace = True)
graduationData.drop(columns=["State"], inplace = True)
graduationData.fillna(method="bfill", axis=1, inplace=True)

# student/teacher ratio data
ratioData = pd.read_csv(ratioPath)
ratioData.set_index(ratioData["State"], inplace = True)
ratioData.drop(columns=["State"], inplace = True)

# minimum wage data
wageData = pd.read_csv(minimumPath)
wageData.set_index(wageData["State"], inplace = True)
wageData.drop(columns=["State"], inplace = True)

# --------------------ADD MAX AND MIN ROWS-------------------- #

# salaryData = pd.concat([salaryData, salaryData.max().transpose()], axis = 1)

# print(salaryData)
print(salaryData.max())
print(pd.DataFrame([salaryData.max(), salaryData.min()], columns=["Max","Min"]).transpose())

exit()

# --------------------ADJUST NUMBERS FOR INFLATION-------------------- #

salary2019Data = masterInflationFunction(salaryData)

wage2019Data = masterInflationFunction(wageData)

# --------------------COMBINE DATA INTO ONE DATAFRAME-------------------- #

allData = pd.concat({
    "Salary": salaryData, 
    "Graduation": graduationData, 
    "Student/Teacher Ratio": ratioData, 
    "Minimum Wage": wageData,
    "Salary 2019 Inflation": salary2019Data,
    "Minimum Wage 2019 Inflation": wage2019Data
}, axis=1)

# print(allData)

# --------------------FLIP INDEX TO HAVE DATA GROUPED BY YEAR-------------------- #

allDataFlipped = allData.reorder_levels([1,0], axis=1).sort_index(level=0, axis=1)

# print(allDataFlipped)

# --------------------FLIP COLUMNS AND ROWS-------------------- #

allDataRotated = allData.transpose()

allDataFlippedRotated = allDataFlipped.transpose()

#----------All States? Testing----------#

widthNumber = 9
heightNumber = 6
states = allData.index

# axArr = allDataRotated.loc["Salary",:].plot.line(subplots=True, layout=(heightNumber,widthNumber), sharex=True, sharey=True, legend = False)

# fig, axArr = plt.subplots(heightNumber, widthNumber)
fig = plt.figure()
fig.set_size_inches(9,6)
gs = fig.add_gridspec(heightNumber, widthNumber, hspace=0.3, wspace=0, top=0.967, right=0.945, left=0.1, bottom=0.136)
axs = gs.subplots(sharex=True, sharey=True)

axArr = fig.axes
maxGrad = allData["Graduation"].max().max()+1
minGrad = allData["Graduation"].min().min()-1

for i in range(len(axArr)): 
    if i < 52:
        state = states[i]
        ax = axArr[i]
        ax.set_title(state,fontdict = {"fontsize": 7}, y=.9)
        allDataRotated.loc["Salary",state].plot.line(ax=ax)
        allDataRotated.loc["Salary 2019 Inflation",state].plot.line(ax=ax)
        allDataRotated.loc["Graduation", state].plot.line(ax=ax,secondary_y=True)
        
        ax.label_outer()
        ax.right_ax.label_outer()
        #x axis good
        ax.tick_params(axis='x',which='both', direction="in", labelrotation=80)
        #make secondary y shared
        ax.right_ax.set_ylim(bottom=minGrad, top=maxGrad)

    elif i == 52:
        ax = axArr[i]
        ax.set_title("Max",fontdict = {"fontsize": 7}, y=.9)
        allData.loc[:,"Salary"].max().plot.line(ax=ax)
        allData.loc[:,"Salary 2019 Inflation"].max().plot.line(ax=ax)
        allData.loc[:,"Graduation"].max().plot.line(ax=ax,secondary_y=True)
        
        ax.label_outer()
        ax.right_ax.label_outer()
        #x axis good
        ax.tick_params(axis='x',which='both', direction="in", labelrotation=80)
        ax.right_ax.set_ylim(bottom=minGrad, top=maxGrad)
    elif i == 53:
        ax = axArr[i]
        ax.set_title("Min",fontdict = {"fontsize": 7}, y=.9)
        allData.loc[:,"Salary"].min().plot.line(ax=ax)
        allData.loc[:,"Salary 2019 Inflation"].min().plot.line(ax=ax)
        allData.loc[:,"Graduation"].min().plot.line(ax=ax,secondary_y=True)
        
        ax.label_outer()
        ax.right_ax.label_outer()
        #x axis good
        ax.tick_params(axis='x',which='both', direction="in", labelrotation=80)
        ax.right_ax.set_ylim(bottom=minGrad, top=maxGrad)
        
        
# print(axArr[0].right_ax.get_lines())
fig.legend(axArr[0].get_lines() + axArr[0].right_ax.get_lines(), ["Salary", "Inflation", "Graduation"])

plt.show()