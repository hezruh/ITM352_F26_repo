# read taxi_1000.csv and calculate the total of all fares, average fare, and max trip distance
import csv

fileName = "taxi_1000.csv"

with open(fileName, "r") as file:
    csvReader = csv.reader(file)

    totalFare = 0.0
    maxDistance = 0.0
    averageFare = 0.0
    numRows = 0

    for row in csvReader:
        if numRows == 0:
            # skip the header row
            fareIndex = row.index("Fare")
            distanceIndex = row.index("Trip Miles")
            numRows += 1
            continue

        if (numRows > 0):
            fare = float(row[fareIndex])
            distance = float(row[distanceIndex])
            totalFare += fare
            if distance > maxDistance:
                maxDistance = distance

        numRows += 1

if numRows > 1:
    averageFare = totalFare / (numRows - 1)  # subtract 1 for the header row

print(f"Total Fare: ${totalFare:.2f}")
print(f"Average Fare: ${averageFare:.2f}")
print(f"Maximum Trip Distance: {maxDistance:.2f} miles")