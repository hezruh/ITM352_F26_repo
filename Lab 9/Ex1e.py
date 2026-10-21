# read the entire file using readlines()
with open("names.txt", "r") as fileObject:
    names = fileObject.readlines()
    print(f"Number of names: {len(names)}")
    for name in names:
        print(name.strip())
        