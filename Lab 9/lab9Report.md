Lab for Chapter 5: File I/O

NOTE: When submitting code, if the code is long or has multiple files, please push it to your GitHub repo and give a direct link to the file or folder. 

1. Create a text file that contains a list of names (one name on each line) and name your file names.txt. 

Write Python code that opens the file using the appropriate file mode and displays the data type returned from open(). Explain why this is more useful than directly working with the file (i.e. immediately read/write).
    https://github.com/hezruh/ITM352_F26_repo/blob/06d8ee538989d98d7d32cf9284c98c6373f8a93e/Lab%209/Ex1.py
    Being able to do it through the open() function is more useful than directly working with the file because it makes it easier to manage file operations and handle errors, as opposed to directly working with the file.

Why is it good practice to close a file after you are done with it? Rewrite the above using with and explain the benefits of working with the file in this manner. 
    It is good practice to close a file after you are done with it in python because if a file is not closed, it can lead to memory leaks or data corruption. Using the with statement automatically handles closing the file for you, even if an error occurs while working with the file.

Using the .read() method, read the names from the names.txt file and print out the names as well as a count of how many names there are altogether. 
    https://github.com/hezruh/ITM352_F26_repo/blob/06d8ee538989d98d7d32cf9284c98c6373f8a93e/Lab%209/Ex1c.py

Rewrite the above using the .readline() method. Explain and give examples of circumstances for which you would use or not use this method over .read()Hint: think about the format of the data. Consider if you needed to read only half of the file. 
    https://github.com/hezruh/ITM352_F26_repo/blob/06d8ee538989d98d7d32cf9284c98c6373f8a93e/Lab%209/Ex1d.py

    If you are only working with a smaller data set, read() by itself works fine. If you are working with an exponentially larger data set, it is more efficient to use readLine() because breaking the data set up line by line will ensure that you only read the data you need, then stop after you are done. For example, if you only needed to read the first 10 lines of a file, using readLine() would be more efficient than reading the entire file into memory with read().

Rewrite the above using the .readlines() method. Explain and give examples of circumstances for which you would use or not use this method over other read methods. Hint: What if you wanted to put the names in a Dictionary? What about efficiency?
    https://github.com/hezruh/ITM352_F26_repo/blob/06d8ee538989d98d7d32cf9284c98c6373f8a93e/Lab%209/Ex1e.py

    the readlines() method is useful when you want to place all of the information within your data set into a list, which, from there, can be converted into a different data structure such as a dictionary. If you are working with a large data set, though, it may be more efficient to use readLine() to read the data line by line instead of reading the entire file into memory at once.

Now add your own name to the end of the file and print the entire contents of the file. ​​What steps are necessary to ensure that the new name is added to the end of the file without losing the existing names? Discuss the pros and cons of appending the file versus overwriting the file.
    https://github.com/hezruh/ITM352_F26_repo/blob/06d8ee538989d98d7d32cf9284c98c6373f8a93e/Lab%209/Ex1f.py

    To ensure the new name is added to the end of the file without losing the existing names, you would have to open the file in append mode (written as "a"). The pros of append is that it won't erase any of the existing data in the file, however if you want to reset your data, you will be unable to do so without switching to write mode (written as "w").

Discuss why the format of the data in a file is important (i.e. block, lines, CSV, JSON, etc.).
    The format of the data in a file is important because different data formats are better for different types of data. For example, if you're working with data that is structured in a table format, you would want to create a CSV file.

2. Ask your AI of choice (e.g. ChatGPT, Gemini, Claude, etc.) the following prompt: “For my company <choose a business e.g. IT consulting>, generate an example 5 row table for a Google Sheet with the following fields: Employee_ID, Age, Annual_Salary, Department_Code, Years_at_Company”. Copy and paste the table into a google spreadsheet and download it to your computer as a csv file named “my_custom_sheet.csv”. Use the Python csv module to load the CSV file and use the data to calculate the average, maximum, and minimum values for the Annual_Salary field. 

Code here:
https://github.com/hezruh/ITM352_F26_repo/blob/06d8ee538989d98d7d32cf9284c98c6373f8a93e/Lab%209/Ex2.py
https://github.com/hezruh/ITM352_F26_repo/blob/06d8ee538989d98d7d32cf9284c98c6373f8a93e/Lab%209/Ex2b.py

What are some advantages and disadvantages of the CSV format?
    Advantages of CSV format can be seen in its simplicity and ease of use. It is a plain text format that is widely supported by many applications, making it easy to share and import/export data. Disadvantages include the lack of support for complex data types, such as nested structures, and the potential for data loss or corruption if the file is not properly formatted.

What Python package enables you to easily get file information such as size and permissions? Look up the documentation on this package and use it to open the file only if it exists and is readable and print out some file information such as size.

    os.

What’s the difference between a text file and a binary file? Under what circumstances would you use one over the other?

    A text file contains ascii or unicode characters meant to be readable by humans, while a binary file contains data in binary format, which computers read. beep beep.

3. Read the 1,000 lines of taxi data from the taxi_1000.csv file and calculate the total of all fares, the average of those fares, and the maximum trip distance (based on the Trip Miles field).
Code here:
    https://github.com/hezruh/ITM352_F26_repo/blob/06d8ee538989d98d7d32cf9284c98c6373f8a93e/Lab%209/Ex3.py

4. ON YOUR OWN: Modify the program in Exercise 3 to calculate the total of all fares, the average of those fares, and the maximum trip distance (based on the Trip Miles field) for records that have fares greater than 10 dollars. 
Code here:


5. Write a program that takes the dictionary of quiz questions you created for Assignment 1 and saves it as a JSON file. 
Code here:


6. Write a program to read the JSON file that you created in question 5 and print it.
Code here:

What are some advantages and disadvantages of the JSON format?




Data file:  taxi_1000.csv
