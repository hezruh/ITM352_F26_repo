# read a csv file containing window cleaning employee data and compute salary stats
# 

import csv
import os

#check if file exists and is readable
if not os.path.exists("employee_data.csv"):
    print("File does not exist.")
    exit(1)

if not os.access("employee_data.csv", os.R_OK):
    print("File is not readable.")
    exit(1)
else:
    fileSize = os.path.getsize('employee_data.csv')
    print(f"file exists and is readable, size: {fileSize} bytes")

csvFileName = "employee_data.csv"
salaries = []

# read the csv file and store the salaries in a list
with open(csvFileName, "r") as csvFile:
    reader = csv.reader(csvFile)
    headers = next(reader)
    print(f"Headers: {headers}")
    salaryIndex = headers.index("Annual_Salary")
    for row in reader:
        salary = float(row[salaryIndex])
        salaries.append(salary)

    # compute salary stats
    avgSalary = sum(salaries) / len(salaries)
    minSalary = min(salaries)
    maxSalary = max(salaries)

    print(f"Average Salary: ${avgSalary:.2f}")
    print(f"Minimum Salary: ${minSalary:.2f}")
    print(f"Maximum Salary: ${maxSalary:.2f}")