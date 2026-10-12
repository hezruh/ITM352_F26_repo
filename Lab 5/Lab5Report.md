Lab for Chapter 3 – from Kaefer pp. 52-58: Dictionaries


1.Write Python code to define a dictionary named taxi_trip_info with the following key value pairs:
 


Print out the dictionary to show what it looks like. Also print out just the Trip_miles value from the dictionary.

Code here:
# Define a dictionary named taxi_trip_info to hold trip information

taxiTripInfo = {
    "tripID" : "da7df362",
    "tripSeconds" : 360,
    "tripMiles" : 1.1,
    "fare" : "$6.25"
}

print("Taxi trip info: ", taxiTripInfo)
print("Trip miles: ", taxiTripInfo["tripMiles"])
print("Fare: ", taxiTripInfo["fare"])

Compare and contrast Dictionaries with Lists
Lists just have index values, dictionaries have key value pairs. You can have strings as the value of keys in dictionaries.



2. Write Python code to define a list of taxi trip durations in miles (use values 1.1, 0.8, 2.5, 2.6). Also define a tuple of fares for the same number of trips (use values “$6.25,” “$5.25,” “$10.50,” “$8.05”). Store both the tuple and the list as values in a dictionary called trips, with keys “miles” and “fares.” Print out the dictionary to show what it looks like.

Code here:


tripDurations = [1.1, 0.8, 2.5, 2.6]
tripFares = ("$6.25", "$5.25", "$10.50", "$8.05")

trips = {
    "miles" : tripDurations,
    "fares" : tripFares
}
print(trips)

print("The duration of the third trip is: ", trips["miles"][2], "miles")
print("The fare of the third trip is: ", trips["fares"][2])

This dictionary could keep a record of several trips by storing all of the trip distances in the list and the corresponding fares in the tuple. The values at the same index describe the same trip. For example, the third trip lasted 2.5 miles and cost $10.50. The list is appropriate for the distances because distances could be added or changed as new trip records are entered.

Look up the zip()function and use it to create a dictionary where the keys are the durations and the values are the fares. You will need to use dict() to create the dictionary from the return value of zip(). Print out the duration and cost of the 3rd trip. Explain if this version is more “elegant” than what you did in (a).
tripDurations = [1.1, 0.8, 2.5, 2.6]
tripFares = ("$6.25", "$5.25", "$10.50", "$8.05")

trips = dict(zip(tripDurations, tripFares))
print(trips)

tripNum = int(input("What trip do you want? "))
print("The duration of your trip is: ", tripDurations[tripNum - 1], " miles")
print("The fare of the trip is: ", tripFares[tripNum - 1])

Create a list of dictionaries where each dictionary represents a trip. Ask Copilot to do this for you. Print out the duration and cost of the 3rd trip. Explain if this version is more “elegant” than what you did in (a) and (b). Discuss the use of regular expressions over manually making the changes. Can you think of a way to write code to make the conversion programmatically (i.e. using the output directly rather than VSCode find and replace)?
trips = [
    {"duration": 1.1, "fare": 6.25},
    {"duration": 0.8, "fare": 5.25},
    {"duration": 2.5, "fare": 10.50},
    {"duration": 2.6, "fare": 8.05}
]

print(trips)
print("The duration of the third trip is: ", trips[2]["duration"], " miles")
print(f'The fare of the third trip is: $(trips[2]["fare"]:.2f)')


Modify your code to use numbers rather than Strings for the fares. Again, you could ask Copilot to do this for you. Note you will have to change how you print the output. Is this better? Why or why not?
This is both better and worse for different ways. Using numbers instead of strings is better if you need to perform operations or compare values
on the fare fees. It's also worse because you now have to manually format your output to include the dollar symbol before the fare price.



3. Go back to the List lab where you appended a tuple of respondent ID values (1012, 1035, 1021, and 1053) list of survey response values (5, 7, 3, and 8) to get 

[5, 7, 3, 8, (1012, 1035, 1021, and 1053)]

We determined that this was a poor design for managing the survey data.  Rather than doing this, create a Dictionary with ID values as the keys and survey responses as the values using zip(). Your dictionary should look like 

{1012: 5, 1035: 7, 1021: 3, 1053: 8}


Code here:
respondentIDs = (1012, 1035, 1021, 1053)
responses = [5, 7, 3, 8]

surveyDict = dict(zip(respondentIDs, responses))
print("Survey dictionary: ", surveyDict)
print("Dictionary keys: ", surveyDict.keys())
print("Dictionary values: ", surveyDict.values())


Discuss why this is a more “usable” data structure than what was done in the prior List lab exercise. Discuss how “ordered” vs. “unordered” data applies to lists and dictionaries.  What might be even more usable?
This is a more usable data structure than the prior exercise as each value (being the responses) are tied to an individual key ID number, instead
of being some index in a long list. This makes it easier to sort and search for individual records based off their IDs instead of some arbitrary
index number.


Consider the following scheme for storing the values of survey responses:

# Assume the highest respondent ID is 50,000 
responses_list = [None] * 50001 
# Storing data for respondent ID 1012 and 48750 
responses_list[1012] = 5 
responses_list[48750] = 3

What are the advantages and drawbacks of using a Python list to store data where the list's index corresponds to a unique ID? Some things to consider: 
What if the IDs are large numbers or not sequential?
What if you didn’t know what the highest respondent ID is (which is common if you are coding the IDs to preserve anonymity)? 
What if the IDs must always be sequential (which is a common way to ensure unique IDs)?
What if the IDs were not Integers (maybe a string like 1011AF)?

The advantages of using a list to store data where the list's index corresponds to a unique ID is that you are able to work with data much faster.
The advantages of using a dictionary to store data instead is that the data is more organized, and you can dynamically allocate just as much memory
as is needed. However, if the data is small in scale, it would be more practical to use a list instead.