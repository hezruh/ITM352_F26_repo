first = input("Enter your first name: ")
middle = input("Enter your middle initial: ")
last = input("Enter your last name: ")

fullName = first + " " + middle + ". " + last
print("Your full name is:", fullName)

print(f"Your full name using f strings is {first} {middle}. {last}")
print("Your full name using percent formatting is %s %s. %s" % (first, middle, last))
print("Your full name using format method is {} {}. {}".format(first, middle, last))
print("Your full name using list joins is " + " hello ".join([first, middle + ".", last]))