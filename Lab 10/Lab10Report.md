Lab: Intro to Numpy and Pandas 


Create a list of tuples that are percentiles and Household Incomes at the specified percentiles for the following table:

Percentile   	Income
10      		14629
20      		25600
30      		37002
40      		50000
50      		63179
60      		79542
70      		100162
80      		130000
90      		184292

 Convert the list into a Numpy Array and report the dimensions of the array and the number of elements in it.
# analyze an array of tuples using numpy
import numpy as np

# create an array of tuples of household income and percentiles
hhIncome = ([
	(10, 14629),
	(20, 25600),
	(30, 37002),
	(40, 50000),
	(50, 63179),
	(60, 79542),
	(70, 100162),
	(80, 130000),
	(90, 184292),
])

hhIncomeArray = np.array(hhIncome)

Print out the table of percentiles and household incomes
# report the dimensios of the array and the num of elements in the array
print(f"dimensions of the array: {hhIncomeArray.ndim}")
print(f"number of elements in the array: {hhIncomeArray.size}")

for i in range(hhIncomeArray.shape[0]):
    percentile, income = hhIncomeArray[i]
    print(f"Percentile: {percentile}, Income: ${income}")

for i in range(hhIncomeArray.shape[0]):
    print(hhIncomeArray[i, 0], hhIncomeArray[i, 1])


Create the following lists:
# List of individuals' ages
ages = [25, 30, 22, 35, 28, 40, 50, 18, 60, 45]


#Lists of individuals' names and genders
names = ["Joe", "Jaden", "Max", "Sidney", "Evgeni", "Taylor", "Pia", "Luis", "Blanca", "Cyndi"]
gender = ["M", "M", "M", "F", "M", "F", "F", "M", "F", "F"]

Use zip() to create a list of (age, gender) tuples.  

Using Pandas, convert the list to a DataFrame, with names as the index and columns Age and Gender. Print out the dataframe and summarize the DataFrame using the describe() method.


Calculate and print out the average age by gender

# create pandas dataframe from individual lists
# do simple stats on the data

import pandas as pd


#Lists of individuals' names, ages, and genders
ages = [25, 30, 22, 35, 28, 40, 50, 18, 60, 45]
names = ["Joe", "Jaden", "Max", "Sidney", "Evgeni", "Taylor", "Pia", "Luis", "Blanca", "Cyndi"]
gender = ["M", "M", "M", "F", "M", "F", "F", "M", "F", "F"]

rawData = zip(ages, gender)

# create a pandas dataframe from the lists
df = pd.DataFrame(data=rawData, index=names, columns=["Age", "Gender"])

summary = df.describe()

print(summary)

# calc avg age by gender
avgAgeByGender = df.groupby("Gender")["Age"].mean()

print("\nAverage age by gender:")
print(avgAgeByGender)


Create a simple dataset using the following dictionary and convert the dictionary to a Pandas DataFrame and print it out:
data = {
   'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
   'Age': [25, 30, 35, 40, 22],
   'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
   'Salary': [70000, 80000, 120000, 90000, 60000]
}

# create a data frame from a dictionary

import pandas as pd

data = {
   'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
   'Age': [25, 30, 35, 40, 22],
   'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
   'Salary': [70000, 80000, 120000, 90000, 60000]
}

# convert the dictionary to a dataframe
df = pd.DataFrame(data)

# display the dataframe
print(df)


Read the json file of taxi trip data at  https://drive.google.com/file/d/1-MpDUIRZxhFnN-rcDdJQMe_mcCSciaus/view?usp=sharing and create a dataframe from it. Print summary statistics about the dataframe, as well as the median.

# Read a JSON file of taxi trip data and create a dataframe and some simple stats

import pandas as pd

df = pd.read_json('Taxi_Trips.json')

# display first few rows of dataframe
print(df.head(6))

# display basic statistics of the dataframe
print(df.describe())

median = df['fare'].median()
print("The median fare value is $", median)


 Read in a CSV file at https://drive.google.com/file/d/1M-X_bypJJ6K5p6eM6aYBwt1qIizIiIex/view?usp=sharing  and turn it into a Pandas dataframe. 
Print out the dimensions of the data frame and show the first 10 rows

Select only properties that have 500 or more units. Drop some unnecessary columns and print the first 10 rows

Look at the data types. Determine which data types are incorrect and coerce them to the correct data type. Look at the data types now and print the cleaned data.

 We have some null values and duplicates.  Drop those rows and print out the results. 

Filter out 0 sales and print the results. Compute and display the average sales price 

import pandas as pd

homesDataFile = 'homes_data.csv'

homesDF = pd.read_csv(homesDataFile)
print(homesDF.head())

shape = homesDF.shape
print("The dimensions of the dataframe are: ", shape)

# only keep properties with more than 500 units and drop the easement column
dfBig = homesDF[homesDF['units'] >= 500]
dfBig = dfBig.drop(columns=['easement'])
print(dfBig.head(10))

# look at the data types
print(dfBig.info())

# coerce land_sqft, gross_sqft, and sale_price to numeric values
dfBig['land_sqft'] = pd.to_numeric(dfBig['land_sqft'], errors='coerce')
dfBig['gross_sqft'] = pd.to_numeric(dfBig['gross_sqft'], errors='coerce')
dfBig['sale_price'] = pd.to_numeric(dfBig['sale_price'], errors='coerce')

# look at the data types and print the cleaned data
print("After cleaning... ")
print(dfBig.info())
print(dfBig.head(10))

# we have some null values. print these
dfBig = dfBig.dropna()

# now drop duplicate records
dfBig = dfBig.drop_duplicates()
print("After dropping nulls and duplicates... ")
print(dfBig.info())
print(dfBig.head(10))

# filter out 0 sales
dfBig = dfBig[dfBig['sale_price'] > 0]
print("After filtering out 0 sales... ")
print(dfBig.info())
print(dfBig.head(10))

What is the purpose of using a CSV file rather than JSON or another data format?
The purpose of using a CSV file rather than JSON or another data format is when you want your data to be readable by humans, as data in CSV files appears as a table/spreadsheet. Additionally, you can easily import CSV files into programs such as Excel and Google Sheets.

From an MIS perspective, why might it be beneficial to use Python/Pandas for data analysis over more end-user driven, no/low code data analysis applications like Excel and Tableau? 
    From an MIS perspective, it may be beneficial to use Python/Pandas for data analyysis in examples where your data to be analyzed is too large and complex to do manually via Excel or Tableau. Also, Python/Pandas is more customizable in regards to what you are able to analyze and how you go about analyzing it.

[on your own] Address the following questions about your experience with Assignment 1:
Did you find Assignment 1 difficult? How?
    Assignment 1 was challenging, however I would not say that it was anywhere near overwhelming in regards to difficulty. The most difficult part for me personally was thinking of questions that fit the different generations (Baby boomers, Millennials, Zoomers, and Gen Alpha) because the answers actually had to be relatable and characteristic of each generation, while still being distinct from one another. 

Do you think the labs and workshop adequately prepared you for successfully completing assignment 1? If not, explain what additional things you needed.
    I do think that the labs and workshop adequately prepared me for successfully completing Assignment 1, particularly the workshop. Based on what we had gone over during the workshop day in class, I was able to generally apply what I had learned in the examples as well as what we had previously done in other labs to complete the Assignment 1.

Did you learn much from your experience doing Assignment 1. Explain what you learned or why you did not learn much. 
    I would say that I am somewhere in the middle; while I did learn how to use FileIO, as it was one of my additional requirements, most of what I had done for the assignment was moreso reinforcing the concepts that we had previously covered in class, such as using input (as well as checking for valid inputs), using loops, and conditional statements.

Discuss your use of AI in working on Assignment 1.
I used AI to help with the comparison of the user's input to their results. Specifically, I had asked Copilot to help me with the formatting of line 98, which functionally checks the generation that the user had earned the most points in, before printing out the name of the generation. After going back and forth trying to figure it out by myself, trying to use zip() and a for loop just as I had used in line 91, I gave up and asked for help from Copilot. However, I have yet to find a way to print a message stating that a tie had occurred between two or more generations. I would like to address this when we revisit Assignment 1 for the interactive interface Assignment.