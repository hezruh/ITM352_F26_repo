# Ask user to enter a decimal number, calculate the square, and display that number back to the user.
# Name: Hezra Calventas
# Date: 9/2/2026

import math

userInputDecimal = float(input("Please enter a decimal number: "))
print(f"You entered: {userInputDecimal}")

square = math.pow(userInputDecimal, 2)
print("The square of ", userInputDecimal, " is: ", square)