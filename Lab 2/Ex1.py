# Asks user for number between 1 and 100, squares it, and prints the result.
# Name: Hezra Calventas
# Date: 9/2/2026
valueEntered = input("give me a whole number between 1 and 100: ")
valueAsInt = int(valueEntered)

valueSquared = valueAsInt ** 2

#print("You entered: ", valueAsInt)
print("You entered: ", valueAsInt," and the square of your number is: ", valueSquared)

print(f"You entered: {valueAsInt} and the square of {valueAsInt} is: {valueSquared}")