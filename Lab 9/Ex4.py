# read taxi_1000.csv and calculate the total of all fares, average fare, and max trip distance
import csv

fileName = "taxi_1000.csv"

with open(fileName, "r") as file:
    csvReader = csv.reader(file)

    totalFare = 0.0
    maxDistance = 0.0
    averageFare = 0.0
    qualifyingRows = 0

    for rowNumber, row in enumerate(csvReader):
        if rowNumber == 0:
            # skip the header row
            fareIndex = row.index("Fare")
            distanceIndex = row.index("Trip Miles")
            continue

        fare = float(row[fareIndex])
        if fare > 10:
            distance = float(row[distanceIndex])
            totalFare += fare
            qualifyingRows += 1
            if distance > maxDistance:
                maxDistance = distance

if qualifyingRows > 0:
    averageFare = totalFare / qualifyingRows

print(f"Total Fare: ${totalFare:.2f}")
print(f"Average Fare: ${averageFare:.2f}")
print(f"Maximum Trip Distance: {maxDistance:.2f} miles")