

tripDurations = [1.1, 0.8, 2.5, 2.6]
tripFares = ("$6.25", "$5.25", "$10.50", "$8.05")

trips = {
    "miles" : tripDurations,
    "fares" : tripFares
}
print(trips)

print("The duration of the third trip is: ", trips["miles"][2], "miles")
print("The fare of the third trip is: ", trips["fares"][2])