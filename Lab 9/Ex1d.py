#read a file of names one at a time and print each name

with open("names.txt", "r") as fileObject:
    while (line := fileObject.readline()):
        print(line.strip())