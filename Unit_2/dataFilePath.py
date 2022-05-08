import os

dirname = os.path.join(os.path.dirname(__file__), "Data")
# filename = os.path.join(dirname, 'Data\\salary.csv')

salaryFileName = "salary.csv"
graduationFileName = "gradRate.csv"
minimumFileName = "minimumWage.csv"
ratioFileName = "ratio.csv"

salaryPath = os.path.join(dirname, salaryFileName)
graduationPath = os.path.join(dirname, graduationFileName)
minimumPath = os.path.join(dirname, minimumFileName)
ratioPath = os.path.join(dirname, ratioFileName)


# mainPath = r"C:\Users\7544501\Documents\School-Data-Science\Unit 2\Data"

# salaryPath = mainPath +"\\" + salaryName
# graduationPath = mainPath +"\\" + graduationName
# minimumPath = mainPath +"\\" + minimumName
# ratioPath = mainPath +"\\" + ratioName
