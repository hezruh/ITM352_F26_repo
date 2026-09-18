# Properly format an inputted name in title case

rawName = input("Enter your name: \n")
strippedName = rawName.strip()
titleCaseName = strippedName.title()
print("Formatted name:", titleCaseName)