# Define a list of survey response values (5, 7, 3, 8) and store them
# in a variable, define a tuple of response IDs (1012, 1035, 1021 and 1053).
# and add these to the list

responseValues = [5, 7, 3, 8]
responseValues.sort()

responseIDs = (1012, 1035, 1021, 1053)
responseValues.append(responseIDs)
print("Combined response values and IDs: ", responseValues)

responseValuesNew = [(1012, 5), (1035, 7), (1021, 3), (1053, 8)]
print("New response values and IDs: ", responseValuesNew)