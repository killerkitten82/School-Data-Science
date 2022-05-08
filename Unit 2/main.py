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

# concat max and min rows after first concating the max and min rows together
salaryData = pd.concat([salaryData, pd.concat([pd.DataFrame(salaryData.max(), columns=["Max"]), pd.DataFrame(salaryData.min(), columns=["Min"])], axis=1).transpose()])
graduationData = pd.concat([graduationData, pd.concat([pd.DataFrame(graduationData.max(), columns=["Max"]), pd.DataFrame(graduationData.min(), columns=["Min"])], axis=1).transpose()])
ratioData = pd.concat([ratioData, pd.concat([pd.DataFrame(ratioData.max(), columns=["Max"]), pd.DataFrame(ratioData.min(), columns=["Min"])], axis=1).transpose()])
wageData = pd.concat([wageData, pd.concat([pd.DataFrame(wageData.max(), columns=["Max"]), pd.DataFrame(wageData.min(), columns=["Min"])], axis=1).transpose()])

# exit()

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

# print(allDataRotated)
# print(allDataFlippedRotated)

#----------All States Line Graph----------#

widthNumber = 9
heightNumber = 6
states = allData.index

# axArr = allDataRotated.loc["Salary",:].plot.line(subplots=True, layout=(heightNumber,widthNumber), sharex=True, sharey=True, legend = False)

fig = plt.figure()
fig.set_size_inches(9,6)
gs = fig.add_gridspec(heightNumber, widthNumber, hspace=0.3, wspace=0, top=0.967, right=0.945, left=0.1, bottom=0.136)
axs = gs.subplots(sharex=True, sharey=True)

axArr = fig.axes
maxGrad = allData["Graduation"].max().max()+1
minGrad = allData["Graduation"].min().min()-1

for i in range(len(axArr)): 
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
    #make secondary y shared manually 
    ax.right_ax.set_ylim(bottom=minGrad, top=maxGrad)
        
fig.legend(axArr[0].get_lines() + axArr[0].right_ax.get_lines(), ["Salary", "Inflation", "Graduation"])

plt.show()
