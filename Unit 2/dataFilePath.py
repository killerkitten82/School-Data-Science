import os

dirname = os.path.join(os.path.dirname(__file__), "Data")
# filename = os.path.join(dirname, 'Data\\salary.csv')

salaryName = "salary.csv"
graduationName = "gradRate.csv"
minimumName = "minimumWage.csv"
ratioName = "ratio.csv"

salaryPath = os.path.join(dirname, salaryName)
graduationPath = os.path.join(dirname, graduationName)
minimumPath = os.path.join(dirname, minimumName)
ratioPath = os.path.join(dirname, ratioName)


# mainPath = r"C:\Users\7544501\Documents\School-Data-Science\Unit 2\Data"

# salaryPath = mainPath +"\\" + salaryName
# graduationPath = mainPath +"\\" + graduationName
# minimumPath = mainPath +"\\" + minimumName
# ratioPath = mainPath +"\\" + ratioName
