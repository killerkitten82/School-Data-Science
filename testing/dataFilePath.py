import os

def getFilePaths(unit):

    dirname = os.path.join(os.path.dirname(os.path.dirname(__file__)), unit, "Data")

    filePathDict = {}

    for file in os.listdir(dirname):
        filePathDict[file[:-4]] = os.path.join(dirname, file)

    return filePathDict


# print(filePathDict)



# print(os.path.dirname(__file__))
# print(os.path.dirname(os.path.dirname(__file__)))
# filename = os.path.join(dirname, 'Data\\salary.csv')

# salaryFileName = "salary.csv"
# graduationFileName = "gradRate.csv"
# minimumFileName = "minimumWage.csv"
# ratioFileName = "ratio.csv"

# salaryPath = os.path.join(dirname, salaryFileName)
# graduationPath = os.path.join(dirname, graduationFileName)
# minimumPath = os.path.join(dirname, minimumFileName)
# ratioPath = os.path.join(dirname, ratioFileName)


# mainPath = r"C:\Users\7544501\Documents\School-Data-Science\Unit 2\Data"

# salaryPath = mainPath +"\\" + salaryName
# graduationPath = mainPath +"\\" + graduationName
# minimumPath = mainPath +"\\" + minimumName
# ratioPath = mainPath +"\\" + ratioName
