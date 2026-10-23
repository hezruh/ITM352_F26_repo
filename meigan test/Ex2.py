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