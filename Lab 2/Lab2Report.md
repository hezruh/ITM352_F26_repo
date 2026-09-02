Lab on Expressions

2.1 Write Python code that uses the input built-in function to ask the user to enter a whole number between 1 and 100. Square the number that the user entered using the exponentiation operator. Print a message to the user stating the value that they entered and the square of the value that they entered. Make sure you correctly handle the data types in the expressions to get the expected results.


Code here:



If you use AI to write code for this, what must you be careful of (go beyond “checking the code is correct” to discussing quality such as comments, style, context, etc.)? Was the generated code appropriate for your level of learning? If not, what followup prompts can you give that would present it at the level that is more helpful? 



List and explain all the expressions in the code (include discussion of variables and operators):



Explain why the input must be converted to an integer data type:
You can't perform arithmetic operations on a string data type.


List example “invalid inputs” and explain how the program would respond to them:



Show one alternative way to print the result message and explain the pros and cons of this approach (hint: there are at least two very different ways):


Extra credit: Explain if a function is an expression and the purpose of this (i.e. being an expression or not an expression).



2.2 Write Python code that uses the input built-in function to ask the user to enter the year they were born as a four-digit number. Print a message to the user stating the value that they entered and their calculated age. Make sure you correctly handle the data types in the expressions to get the expected results.

Code here:


Why might the calculated age not be correct and what can be done to address this:


If birthyear is a variable used to store the converted input, what’s wrong with the expression "Your age is " + birthyear:


Explain why the names of the variables are good or not good and explain why good naming is important:



2.3 Write Python code that uses the input built-in function to ask the user to enter a decimal formatted number between 1 and 100. Square the number that the user entered using the exponentiation operator. Print a message to the user stating the value that they entered and the square of the value that they entered.

Code here:


Explain how casting was used and why it was necessary:



Research alternative ways to square the inputted value that do not use the exponentiation operator and explain why you may want to use such alternatives:



Add or adjust comments to your code. Explain why you added these and how they are important/useful:



2.4 Modify the code in Exercise 2.3 to round the values reported to the user to two decimal places (use the round built-in function).

Before you write the code, look up some documentation on the round() function. What data type is the return value and why is it this data type? How do you know this? Do you think another data type might be better?


Code here:



2.5 Write Python code that uses the input built-in function to ask the user to enter a sentence of their choosing. Use the len built-in function to determine how many characters were in the string entered and report this information back to the user.

Code here:



Implement an example of using the sentence that requires the length of a string in an expression e.g. printing the middle character in the sentence (you cannot use this as your example). Code here:



2.6 Write Python code that uses the input built-in function to ask the user to enter a weight in pounds. The input function always returns a string value, so use the float built-in function to convert the value entered to a float data type and determine the equivalent weight in kilograms (you can use the conversion factor that 1 pound = 0.453592 kilograms). Print a message to the user stating the weight in pounds that they entered and the equivalent weight in kilograms.

Write the program using one line of code. Code here:



Discuss the pros and cons of implementing it in one line:




2.7 Write Python code that uses the input built-in function to ask the user to enter a temperature in the Fahrenheit temperature scale. The input function always returns a string value, so use the float built-in function to convert the value entered to a float data type and determine the equivalent temperature in the Celsius temperature scale (use the conversion factor °C = (°F – 32) × (5/9)). Print a message to the user stating the temperature in Fahrenheit that they entered and the equivalent temperature in Celsius. You can verify that your code executes properly by entering in 32°F (equivalent is 0°C) and 212°F (equivalent is 100°C).

Code here:


Why do you want to verify your code using the input 32°F? What is it called when you do this kind of verification?


Are there other verifications that should be done? Explain:



Re-write the program as a function and test the function:



Explain the pros and cons of creating a function to do the conversion:
