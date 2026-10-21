# add your own name to file
with open("names.txt", "r") as fileObject:
    contentsList = fileObject.readlines()
    print(contentsList)

userName = input("Enter your name: ")

with open("names.txt", "a") as fileObject:
    print(f"Adding {userName} to file")
    fileObject.write(f"\n{userName}\n")
