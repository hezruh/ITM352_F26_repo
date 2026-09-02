# Ask user to enter a decimal number, calculate the square, and display that number back to the user.
# Then round it to two decimal places and print it out.
# Name: Hezra Calventas
# Date: 9/2/2026

import math

userInputDecimal = float(input("Please enter a decimal number: "))
square = math.pow(userInputDecimal, 2)
roundedSquare = round(square, 2)

print(f"You entered: {userInputDecimal}")
print("The square of ", userInputDecimal, " is: ", roundedSquare)