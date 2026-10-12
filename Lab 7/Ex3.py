data = ("hello", "10", "goodbye", 3, "goodnight", 5)

strCount = 0
for item in data:
    if type(item) == str:
        strCount += 1

print(f"There are {strCount} strings in the tuple.")