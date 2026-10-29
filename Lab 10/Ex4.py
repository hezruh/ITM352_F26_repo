# Read a JSON file of taxi trip data and create a dataframe and some simple stats

import pandas as pd

df = pd.read_json('Taxi_Trips.json')

# display first few rows of dataframe
print(df.head(6))

# display basic statistics of the dataframe
print(df.describe())

median = df['fare'].median()
print("The median fare value is $", median)