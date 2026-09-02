valueEntered = input("give me a whole number between 1 and 100: ")
valueAsInt = int(valueEntered)

valueSquared = valueAsInt ** 2

#print("You entered: ", valueAsInt)
print("You entered: ", valueAsInt," and the square of your number is: ", valueSquared)

print(f"You entered: {valueAsInt} and the square of {valueAsInt} is: {valueSquared}")