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