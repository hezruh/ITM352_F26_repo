1. Write Python code that initializes a tuple of strings representing different emotions (i.e., happy, sad, fear, surprise). Write code that uses a conditional expression (do not use an if-statement or ternary expression) to print “true” if the last element is “happy” and there are more than 3 elements, or “false” if it is not. (Hint: You can use the len function to determine how many elements are in the tuple and then use that information in the expression). 

Code here:
emotions = ("surprise", "sad", "fearful", "happy", "anxious")

print(emotions[-1] == "happy" and len(emotions) > 3)



Rewrite the code using an if-statement
if emotions[-1] == "happy" and len(emotions) > 3:
    print("True")
else:
    print("False")

Explain the advantages/disadvantages of (a) and (b)
A is more compact, if you need to optimize your code as much as humanly possible or just want to make it as few lines as possible, you would go with a. B is more readable, and in my opinion I would rather write B as it is just easier to glance at and understand what the code does.

2. ON YOUR OWN: Write Python code that creates a list with a variety of different values. Include control logic (if, elif, else) that will print different messages whether the list contains fewer than 5 elements, between 5 and 10 (inclusive), and more than 10 elements. Test your code on lists with several different lengths.

Code here:
test_lists = [
    ["apple", 42, 3.14],
    ["red", 7, True, "blue", 2.5],
    [1, "two", 3.0, False, "five", 6, "seven", 8.0, "nine", 10, "eleven", 12],
]
if len(values) < 5:
    print("Fewer than 5 elements")
elif len(values) <= 10:
    print("Between 5 and 10 elements")
else:
    print("More than 10 elements")

What are the conditional expressions used?

The conditional expressions are len(values) < 5 and len(values) <= 10.

Create a list of lists with test cases for each possible condition. Use this list to test that the code behaves as expected. Tip: try asking ChatGPT to generate the test cases.

How could you write the code to make task (c) more efficient and flexible?

You would use a for loop.


3.  Write the Python conditional logic to determine a movie price for a theater chain. The applicable business rules are:
- The normal price is $14
- If someone is 65 or older, they pay $8.
- If it is Tuesday, the price is $10.
- If it is a matinee, the price is $5 for seniors and $8 otherwise

Create variables for age (an integer), weekday (a string, e.g. “Monday”, “Friday” etc.), and matinee (a boolean).  Print out the values of the variables and the calculated price. The price should always be the lowest one that applies:

# determine the movie price. rules are:
"""
normal price = $14
65+, $8
tues, $10
matinee, price = $5 for seniors, $8 otherwise
Name: Hezra Calventas
Date: Sep 25, 2026
"""

age = 82
day = "Tuesday"
matinee = True

price = 14

if day == "Tuesday":
    price = 10

if age >= 65:
    price = 8

if matinee:
    if age >= 65:
        price = 5
    else:
        price = 8

print("Ticket price is $", price)

print(f"Day: {day}, Matinee: {matinee}")
if age >= 65:
    print("welcome boomer")
else:
    print("welcome zoomer")

print(f"Ticket price is ${price:.2f}")



4. A leap year is a year that consists of 366 days, not the usual 365 days. It occurs roughly every four years, with the exception of certain century years. Specifically, a year is a leap year if it is either 1) evenly divisible by 4 but not divisible by 100, or 2) evenly divisible by 400. Here is a diagram of the conditional logic (this is a “flow chart”):

year = int(input("give me a year\n"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, " is a leap year.")
        else:
            print(year, "is not a leap year.")
    else:
        print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")


Design a conditional expression for the leap year conditional logic using a combination of AND and OR operators with specific parenthetical grouping (Condition A AND Condition B) OR Condition C. How must you ensure that the boolean operators correctly mirror the flow-chart to prevent unintended evaluation order? 

You would have to put the boolean checks in the exact order that the flowchart says (ie. if year % 4 == 0 AND if year % 100 == 0...).

Test your program with your own birth year and the closest leap year to your birth year. If your birth year is a leap year, then use your birth year + 1 for the non-leap year. 


Create a function isLeapYear() that takes a year (a positive integer) as a parameter  and returns either "Leap year" or "Not a leap year.” Implement this using if-statements rather than the conditional expression in (a). Test your function as in (a). Discuss the design considerations in developing the if-statements (use of if-else, order of conditionals, use of early return versus storing value, etc.).

Developing the if-statements is all going to be similar in a runtime scenario, as we haven't gotten to switch statements (which are called matches in python). For the order of conditionals, nested if-else statements would have to check the condition each time before proceeding to the next conditional, while making one long conditional using AND/OR would execute all at once, though would strictly adhere to the sequence in which the conditional was written.

Although the task only asks for a positive integer year, if this function were used commercially, what essential design considerations must be applied to handle potential problematic inputs to the function?

You can check for if the program runs into an error casting the inputted value into an int, such as a person typing the year out in letters; you can also check to ensure they don't put a negative value or infinity. You can also nest the if statement that checks for a valid input inside of a while loop so that the program keeps asking until it gets a value it can work with.



5. An assertion in Python is a statement that checks whether a condition you believe should be true actually is true at that point in the program. You write them using the assert keyword.  The form is:

assert condition, "optional message shown if it fails"

This means that assertions are, like if statements, used to check conditions in a program.  

Create a function celsius_to_fahrenheit that takes a temperature in celsius and returns it in fahrenheit.

Add an assertion that will cause the program to terminate and raise an exception if the temperature is below absolute zero (-273.15C).

# Testing the use of assertions

def celsiusToFahrenheit(celsius):
    #convert Celsius to Fahrenheit
    assert celsius >= -273.15, "Temperature cannot be below absolute zero."
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

print(celsiusToFahrenheit(0)) # should print 32.0
print(celsiusToFahrenheit(100)) # should print 212.0
print(celsiusToFahrenheit(-300)) # should raise AssertionError


Describe some cases in a program where you would want to use assertions.
You could use an assertion to quickly check for if an inputted value was valid or not. You could also use it to maybe check for a runtime error in your program? I'm not sure.