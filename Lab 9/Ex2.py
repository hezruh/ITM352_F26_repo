#

import csv

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