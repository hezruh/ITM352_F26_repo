Lab on Expressions

2.1 Write Python code that uses the input built-in function to ask the user to enter a whole number between 1 and 100. Square the number that the user entered using the exponentiation operator. Print a message to the user stating the value that they entered and the square of the value that they entered. Make sure you correctly handle the data types in the expressions to get the expected results.


Code here:
# Asks user for number between 1 and 100, squares it, and prints the result.
# Name: Hezra Calventas
# Date: 9/2/2026
valueEntered = input("give me a whole number between 1 and 100: ")
valueAsInt = int(valueEntered)

valueSquared = valueAsInt ** 2

#print("You entered: ", valueAsInt)
print("You entered: ", valueAsInt," and the square of your number is: ", valueSquared)

print(f"You entered: {valueAsInt} and the square of {valueAsInt} is: {valueSquared}")


If you use AI to write code for this, what must you be careful of (go beyond “checking the code is correct” to discussing quality such as comments, style, context, etc.)? Was the generated code appropriate for your level of learning? If not, what followup prompts can you give that would present it at the level that is more helpful? 

    We wrote the code together in class.


List and explain all the expressions in the code (include discussion of variables and operators):
    1. `input("give me a whole number between 1 and 100: ")` - This is a function call that prompts the user for input and returns a string.
    2. `int(valueEntered)` - This is a function call that converts the string input to an integer.
    3. `valueAsInt ** 2` - This is an arithmetic expression that raises the integer to the power of 2.
    4. `print("You entered: ", valueAsInt," and the square of your number is: ", valueSquared)` - This is a function call that prints the values of the variables.
    5. `print(f"You entered: {valueAsInt} and the square of {valueAsInt} is: {valueSquared}")` - This is a formatted string literal that prints the values of the variables.

Explain why the input must be converted to an integer data type:
    You can't perform arithmetic operations on a string data type.


List example “invalid inputs” and explain how the program would respond to them:
    1. If the user enters a non-numeric value, the `int()` function will raise a `ValueError`.
    2. If the user enters a number outside the specified range (1-100), the program will still execute but with an unexpected result.

Show one alternative way to print the result message and explain the pros and cons of this approach (hint: there are at least two very different ways):
    print(f"You entered: {valueAsInt} and the square of {valueAsInt} is: {valueSquared}")

    print(f) uses a different approach, as it's a formatted string using curly braces instead of just concatenating strings.


Extra credit: Explain if a function is an expression and the purpose of this (i.e. being an expression or not an expression).
    It is an expression because it returns a value at the end of the function call.


2.2 Write Python code that uses the input built-in function to ask the user to enter the year they were born as a four-digit number. Print a message to the user stating the value that they entered and their calculated age. Make sure you correctly handle the data types in the expressions to get the expected results.

Code here:
    # Ask user to enter the year they were born, and calculate their age based on the current year (2026).
# Name: Hezra Calventas
# Date: 9/2/2026

yearOfBirth = int(input("Please enter the year that you were born: "))
currentYear = 2026
print(f"You were born in {yearOfBirth} and you are {currentYear - yearOfBirth} years old.")

Why might the calculated age not be correct and what can be done to address this:
    The calculated age might not be correct if the user has not yet had their birthday this year. To address this, you could ask the user for their birth month and day, and compare it to the current date to determine if they have had their birthday yet.

If birthyear is a variable used to store the converted input, what’s wrong with the expression "Your age is " + birthyear:
    The variable birthyear is an integer, and you cannot concatenate a string with an integer directly. 

Explain why the names of the variables are good or not good and explain why good naming is important:
    They're good; you need good names because it makes your code readable whenever someone else looks at it, or if you look at it again weeks later.


2.3 Write Python code that uses the input built-in function to ask the user to enter a decimal formatted number between 1 and 100. Square the number that the user entered using the exponentiation operator. Print a message to the user stating the value that they entered and the square of the value that they entered.

Code here:
    # Ask user to enter a decimal number, calculate the square, and display that number back to the user.
# Name: Hezra Calventas
# Date: 9/2/2026

import math

userInputDecimal = float(input("Please enter a decimal number: "))
print(f"You entered: {userInputDecimal}")

square = math.pow(userInputDecimal, 2)
print("The square of ", userInputDecimal, " is: ", square)

Explain how casting was used and why it was necessary:
    
    Casting was used to convert the user input from a string to a float using the `float()` function. 


Research alternative ways to square the inputted value that do not use the exponentiation operator and explain why you may want to use such alternatives:
    You can use math.pow() which is a function that raises a number to a specified power.


Add or adjust comments to your code. Explain why you added these and how they are important/useful:
    It makes your code more readable/understandable in natural language.


2.4 Modify the code in Exercise 2.3 to round the values reported to the user to two decimal places (use the round built-in function).

Before you write the code, look up some documentation on the round() function. What data type is the return value and why is it this data type? How do you know this? Do you think another data type might be better?

    The return value of the round() function is a float.


Code here:
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



2.5 Write Python code that uses the input built-in function to ask the user to enter a sentence of their choosing. Use the len built-in function to determine how many characters were in the string entered and report this information back to the user.

Code here:
    sentence = input("Enter a sentence of your choosing: ")
characterCount = len(sentence)

print(f"Your sentence contains {characterCount} characters.")



Implement an example of using the sentence that requires the length of a string in an expression e.g. printing the middle character in the sentence (you cannot use this as your example). Code here:

sentence = input("Enter a sentence of your choosing: ")
characterCount = len(sentence)

print(f"Your sentence contains {characterCount} characters.")

print("-" * len(sentence))

2.6 Write Python code that uses the input built-in function to ask the user to enter a weight in pounds. The input function always returns a string value, so use the float built-in function to convert the value entered to a float data type and determine the equivalent weight in kilograms (you can use the conversion factor that 1 pound = 0.453592 kilograms). Print a message to the user stating the weight in pounds that they entered and the equivalent weight in kilograms.

Write the program using one line of code. Code here:
weightPounds = float(input("Enter your weight in pounds: ")); print(f"You entered {weightPounds} pounds, which is equivalent to {weightPounds * 0.453592} kilograms.")


Discuss the pros and cons of implementing it in one line:
    pros: It saves space.
    cons: It's really hard to read.



2.7 Write Python code that uses the input built-in function to ask the user to enter a temperature in the Fahrenheit temperature scale. The input function always returns a string value, so use the float built-in function to convert the value entered to a float data type and determine the equivalent temperature in the Celsius temperature scale (use the conversion factor °C = (°F – 32) × (5/9)). Print a message to the user stating the temperature in Fahrenheit that they entered and the equivalent temperature in Celsius. You can verify that your code executes properly by entering in 32°F (equivalent is 0°C) and 212°F (equivalent is 100°C).

Code here:
    # Ask user to enter a temperature in Fahrenheit and convert it to Celsius.
# Name: Hezra Calventas
# Date: 9/4/2026

fahrenheit = float(input("Enter a temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * (5 / 9)

print(f"{fahrenheit}°F is equivalent to {celsius}°C.")


Why do you want to verify your code using the input 32°F? What is it called when you do this kind of verification?
    32F is equal to 0C, which is the freezing point of water. This is called a test case.

Are there other verifications that should be done? Explain:
    212F is equal to 100C, which is the boiling point of water. This is another test case that can be used to verify the accuracy of the conversion formula. 


Re-write the program as a function and test the function:
    def fahrenheitToCelsius(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)


    # Test the function with known temperature conversions.
    print(f"32°F is {fahrenheitToCelsius(32)}°C")
    print(f"212°F is {fahrenheitToCelsius(212)}°C")
    print(f"98.6°F is {fahrenheitToCelsius(98.6)}°C")


Explain the pros and cons of creating a function to do the conversion:

    you just need to call the function, not write the code over and over.
