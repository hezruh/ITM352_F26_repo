
with open("names.txt", "r") as fileObject:
    contents = fileObject.read()
    print(contents)
    contentsList = contents.split("\n")
    print(f"Number of contents: {len(contentsList)}")
    for name in contentsList:
        print(name)