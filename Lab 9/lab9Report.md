Lab for Chapter 5: File I/O

NOTE: When submitting code, if the code is long or has multiple files, please push it to your GitHub repo and give a direct link to the file or folder. 

1. Create a text file that contains a list of names (one name on each line) and name your file names.txt. 

Write Python code that opens the file using the appropriate file mode and displays the data type returned from open(). Explain why this is more useful than directly working with the file (i.e. immediately read/write).

Why is it good practice to close a file after you are done with it? Rewrite the above using with and explain the benefits of working with the file in this manner. 

Using the .read() method, read the names from the names.txt file and print out the names as well as a count of how many names there are altogether. 
 
Rewrite the above using the .readline() method. Explain and give examples of circumstances for which you would use or not use this method over .read()Hint: think about the format of the data. Consider if you needed to read only half of the file. 

Rewrite the above using the .readlines() method. Explain and give examples of circumstances for which you would use or not use this method over other read methods. Hint: What if you wanted to put the names in a Dictionary? What about efficiency?

Now add your own name to the end of the file and print the entire contents of the file. ​​What steps are necessary to ensure that the new name is added to the end of the file without losing the existing names? Discuss the pros and cons of appending the file versus overwriting the file.

Discuss why the format of the data in a file is important (i.e. block, lines, CSV, JSON, etc.).


2. Ask your AI of choice (e.g. ChatGPT, Gemini, Claude, etc.) the following prompt: “For my company <choose a business e.g. IT consulting>, generate an example 5 row table for a Google Sheet with the following fields: Employee_ID, Age, Annual_Salary, Department_Code, Years_at_Company”. Copy and paste the table into a google spreadsheet and download it to your computer as a csv file named “my_custom_sheet.csv”. Use the Python csv module to load the CSV file and use the data to calculate the average, maximum, and minimum values for the Annual_Salary field. 

Code here:

What are some advantages and disadvantages of the CSV format?

What Python package enables you to easily get file information such as size and permissions? Look up the documentation on this package and use it to open the file only if it exists and is readable and print out some file information such as size.

What’s the difference between a text file and a binary file? Under what circumstances would you use one over the other?


3. Read the 1,000 lines of taxi data from the taxi_1000.csv file and calculate the total of all fares, the average of those fares, and the maximum trip distance (based on the Trip Miles field).
Code here:


4. ON YOUR OWN: Modify the program in Exercise 3 to calculate the total of all fares, the average of those fares, and the maximum trip distance (based on the Trip Miles field) for records that have fares greater than 10 dollars. 
Code here:


5. Write a program that takes the dictionary of quiz questions you created for Assignment 1 and saves it as a JSON file. 
Code here:


6. Write a program to read the JSON file that you created in question 5 and print it.
Code here:

What are some advantages and disadvantages of the JSON format?




Data file:  taxi_1000.csv
