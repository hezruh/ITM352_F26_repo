# open a file using 'with'

with open("names.txt", "r") as fileObject:
    print(type(fileObject))

print("file is closed?", fileObject.closed)