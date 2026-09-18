Lab Part a: Lists, Strings, Tuples

1. Use the input() function to input three strings (a first name, a middle initial, and a last name). Concatenate these strings together with a space between each, storing the result in a new variable. Print out the concatenated string.

Do this using the “+” concatenation operator. Explain how Python knows this is different than adding two numbers together.

Do this using an f-string 

Do this using the % Operator

Do this using the format() method for a string

Do this using a join() method of a list

Do this using the format() method for a string but unpacking the list as the argument

first = input("Enter your first name: ")
middle = input("Enter your middle initial: ")
last = input("Enter your last name: ")

fullName = first + " " + middle + ". " + last
print("Your full name is:", fullName)

print(f"Your full name using f strings is {first} {middle}. {last}")
print("Your full name using percent formatting is %s %s. %s" % (first, middle, last))
print("Your full name using format method is {} {}. {}".format(first, middle, last))
print("Your full name using list joins is " + " ".join([first, middle + ".", last]))


2. Define a list of survey response values [5, 7, 3, and 8] and store them in a variable. Next define a tuple of respondent ID values (1012, 1035, 1021, and 1053). Use the .append() method to append the tuple to the list. Print out the list. 


Code here:

# Define a list of survey response values (5, 7, 3, 8) and store them
# in a variable, define a tuple of response IDs (1012, 1035, 1021 and 1053).
# and add these to the list

responseValues = [5, 7, 3, 8]
responseValues.sort()

responseIDs = (1012, 1035, 1021, 1053)
responseValues.append(responseIDs)
print("Combined response values and IDs: ", responseValues)

responseValuesNew = [(1012, 5), (1035, 7), (1021, 3), (1053, 8)]
print("New response values and IDs: ", responseValuesNew)



Explain the output. 
The first print statement, "Combined response values and IDs:  [3, 5, 7, 8, (1012, 1035, 1021, 1053)]", simply adds whatever is in the responseIDs tuple into the end of the list.
The second print statement, "New response values and IDs:  [(1012, 5), (1035, 7), (1021, 3), (1053, 8)]", creates a new list of tuples that combines the response IDs with the
corresponding response values.

Discuss how you might make use of the list and what problems you might have using it.
For taking in and changing the survey data, the lists of touples would be more useful. However, if you wanted to sort the data by response value, you would have to write a custom sort function to sort the list of tuples by the second element in each tuple.

What might be a better way to store survey response values and their respective respondent ID values?
A dictionary would likely be a better way to store survey response values and their respective respondent ID values because having a value and key system would make it easier to look up a response value based on a respondent ID and vice versa.


Compare and contrast a List object with a String object 
A list object is mutable, meaning that you can change the values that are stored in the list after it's made. On the other hand, a String object is what is known as immutable, meaning that once you create the string, you cannot change the values that are stored in it. Also, a list can hold multiple data types, while a string can only hold characters.

Look up some documentation or tutorial on Arrays in Python. Compare and contrast with a List object. Explain why you might want to use an array instead of a list.
Lists are more flexible than arrays because they can hold multiple data types, while arrays can only hold one data type. However, arrays are more efficient in terms of memory and performance when dealing with large amounts of data of the same type. If you know that all of your data will be an integer, for example, and you need to perform a lot of mathematical operations on that data, an array would be a better choice than a list.


3. Create the list of responses from Exercise 2 (values 5, 7, 3, 8). Next add the response “0” to the end of the list using the .append() method. Next add the response “6” to the list between the values 7 and 3 (in what will be the third position in the list) using the .insert() method. Print out the list to verify that you made the changes 
correctly.


Code here:
# Manipulate a list in various tricky ways
# Name: Hezra Calventas
# Date: September 16, 2026

responseValues = [5, 7, 3, 8]
responseValues.append(0)
print("Response values after appending 0: ", responseValues)
# responseValues.insert(2, 6)
responseValues = responseValues[:2] + [6] + responseValues[2:]
print("Response values after inserting 6 at index 2: ", responseValues)



Do the same operations using list slicing (e.g. [:2]) and the “+” operator rather than .insert(). Explain what the “+” operator does on lists compared to strings and numbers.
In a list, the "+" operator creates a new list that combines the elements of the two lists being added together. When used with strings, the "+" operator concatenates/combines the strings together, and when used with numbers, it adds.


Why might you use list slicing over .insert()?
If you're replacing multiple values at once, you would use list slicing. If you're only replacing one value, you would use .insert().


4.  Create the tuple of survey respondent IDs from Exercise 3 (1012, 1035, 1021, and 1053). Next attempt to add the respondent ID “1011” to the end of the tuple using the .append() method. 

Code here:
# Try to append a tuple. It won't work.
# Name: Hezra Calventas
# Date: September 16, 2026

surveyRespondents = (1012, 1035, 1021, 1053)
# surveyRespondents.append(1054)
surveyRespondents = surveyRespondents + (1054,)
print("Updated survey respondents: ", surveyRespondents)

What happens when you attempt to run the code? Explain the problem.
AttributeError: 'tuple' object has no attribute 'append'. The values inside of a touple cannot be changed after they are created, so you cannot use the .append() method to add a new value to the end of the tuple. 

 Address the problem above using the “+” operator with the tuple (1011,). Why could you not just use 1011 or (1011)?
A tuple needs a comma after the first element to distinguish it from a single value in parentheses.

Compare and contrast tuples and lists
While lists can be changed after they are created, tuples cannot be changed. Also, lists are signified by square brackets, whereas tuples are signified by parentheses.

Why do you think tuples are not changeable (immutable)?
Tuples are not changeable because they are not designed to be that way. They are designed to be a fixed collection of values. Basically, because python said so.