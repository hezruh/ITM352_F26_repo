Lab for Chapter 2: Functions and Modules


Installing and using function libraries (modules).
 See if the cryptography library is installed using pip show cryptography. If not,  pip install cryptography. Write a small program using import that tests that the library was installed correctly. Put your code and results here:

# Exercise 1: Introduction to Cryptography
# Name: Hezra Calventas
# Date: 9/9/2026

import cryptography

print(cryptography.__version__)



Using online documentation, find and read the documentation for an appropriate function that might be used to encrypt then decrypt a string. Change your import to specifically load the library with this function (hint: use from cryptography.xxx import xxx where xxx is the library with the encrypt function).  Use the function to encrypt and decrypt a string input from the user. Note that the string will need to be “encoded” before encrypting it and decoded after decryption. Code and results here and explain why the string needs to be encoded and decoded:

    # Exercise 1b: Fernet Encryption
# Name: Hezra Calventas
# Date: 9/9/2026

from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipherSuite = Fernet(key)

encodedText = cipherSuite.encrypt(b"Hello, World!")
print("Encoded Text:", encodedText)
decodedText = cipherSuite.decrypt(encodedText)
print("Decoded Text:", decodedText)



How many parameters does the encryption function take?  How do you know what the parameters are and what values they expect? Is it necessary to place the parameters in a certain order? Why/why not? 

    one parameter, the function signature in the documentation tells me.
    the values they expect are a byte string, and the order is important because the function signature specifies the order of parameters.



Is the function named appropriately? Explain why or why not.

    it is named appropriately because it states that the function is used to encrypt a string, which is what happens.


Explain why it is not necessary to give the key string as a parameter to the encode/decode functions. How does this work and why this is better than putting the string directly in the function call? Why is this different than the encryption/decryption functions where you do have to put the string in as an argument?
    
    It is not necessary to give the key string as a parameter to the encode/decode functions because the key is already associated with the cipherSuite object.

Create a function—call it midpoint —that takes two numbers as input and returns the value halfway between them. 
Code here:

'''
Create a function—call it midpoint —that takes two numbers as input and returns the value halfway between them. 
'''
num1 = int(input("Enter the lower number: "))
num2 = int(input("Enter the higher number: "))

def midpoint(num1, num2):
    return int((num1 + num2) / 2)

print(f"The midpoint between {num1} and {num2} is: {midpoint(num1, num2)}")



Explain the benefit of creating this function:

You don't have to write the formula over and over again each time you want to do that operation.`

Explain if the function is named appropriately:

It's named appropriately because it describes what the function does, which is to find the midpoint between two numbers.


Create a function—call it squareroot—that takes a number and returns the square root of that number. Use the fact that the square root of n is n**0.5.

Code here:


Explain why we might create this function rather than use n**0.5 whenever we want the squareroot:


Now that you have two functions, create a new “module”, called HandyMath.py, and put your two functions into that module.  Now add three more handy math functions: 
exponent, which takes two numbers, a base and an exponent, and returns the value when you raise the base to the power of the exponent. Code here:

max, which takes two numbers as input and returns the value of the larger one. Use the two comparison expressions or a conditional expression (do not use an if-statement). Code here:


min, which takes two numbers as input and returns the value of the smaller one. Use the two comparison expressions or a conditional expression (do not use an if-statement). Code here:



Create a new file, call it Use_Module.py, that imports HandyMath.py, asks for two numbers from a user, and prints out the midpoint of those numbers, the square root of the square of one number, the result when raising one number to the exponent of the other, and finally the max and min of the numbers. Use the Python f-string capability to format these strings. 
Code here:


Explain the benefits of creating and using this custom module:



a. Look up the math functions built into Python (https://www.w3schools.com/python/python_math.asp).  Have you replicated any of those functions in HandyMath? 


b. Look up the math module (https://docs.python.org/3/library/math.html). Have you replicated any of those functions in HandyMath?


c. Change your import to from HandyMath import max, min and rewrite and test your code. Explain how you are able to use HandyMath module functions in place of the built-in and math module functions. Also, explain how you know which function is being used.


(Extra Credit) 
Add a function to your HandyMath module that takes two numbers x,y and a function name as arguments then returns a string “The function <function name> x,y = <function applied to x,y>”. You can use .__name__ to get the identifier of a variable. Try this out for min, max, and exponent. Code here:


What does this tell you about functions in Python?


Is there any benefit to passing functions as arguments to another function? Can you think of an example where this would be useful? Hint: Why might I want to give a callback function for a function rather than return a value?



[on your own] Prompt co-pilot to create a function that converts temperatures to and from celsius, fahrenheit, and kelvin. The function should take as an argument a conversion function rather than ask the user what conversion to make. Give an assessment of this function in terms of the pros and cons of how it was implemented and when you would prefer using this implementation over individual fixed conversion functions. Use co-pilot to give its assessment and compare with your assessment. Did you note anything it did not? Did it note something you did not?
