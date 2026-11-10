Lab: Pivot tables with Pandas

Using Pandas, read in a CSV file with sales data, called sales_data.csv into a dataframe and print the first 5 rows and show the data types of the columns. The file can be found here:  
https://drive.google.com/file/d/1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K/view?usp=drive_link 

This is the URL you can use to directly access the file using pd.read_csv()

https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K

Note: If you have not already done so, you will need to install Pandas and pyarrow for this to work.

Note2: If you are unable to successfully load the data from the Google Drive you may download and load the data locally for the purposes of this lab. However, you will need diagnose and address this problem since you will be required to load the data from the Google Drive for Assignment 2.

Read the CSV file from the URL using exception handling and convert the data types using the pyarrow data type backend. Have it skip bad lines read in. Explain why you want to do these things (exception handling, pyarrow conversion, skip bad lines). Explain why it’s better to convert the data while it is read rather than after. If you received warnings, how do you address these?

I used exception handling so that the program would display an error instead of stopping unexpectedly if the file could not be read. I used the pyarrow data type backend because it gives Pandas more efficient data types for working with a large dataset. I used "on_bad_lines='skip'" so that rows with formatting problems would not prevent the rest of the valid data from being loaded. Converting the data while it is being read is better because the dataframe is cleaned earlier and does not need another separate conversion step afterward. If I received warnings, I would read what caused each warning and adjust the "read_csv()" options or clean the specific column that caused it instead of ignoring the warning.

Use Pandas to convert the order_date column into a standard date representation. Why do you want to do this? If you received warnings, how do you address these?

I converted the "order_date" column into a standard date representation so that Pandas would recognize the values as dates instead of strings. This makes it easier to sort the orders, filter by dates, and group the data by month or year. If I received a warning about inconsistent date formats, I would specify the expected format when using "pd.to_datetime()" or use "errors='coerce'" to turn invalid dates into missing values that I could check afterward.



Adding to the program you created in 1. Create a pivot table out of this data, aggregating sales by region, with columns defined by order_type (which is either Retail or Wholesale) and totals column (i.e. “margins”). You must create a new sales column in the dataframe from the quantity and unit_price columns (sales = quantity * price) before creating the pivot table.  Use Pandas to_numeric to coerce quantity and unit_price to numeric before computing sales. Explain why you should do this. Use the numpy sum function rather than the built-in sum function. Set the Panda option "display.max_columns", None, to force the display of all columns. Explain what this does and if you need to do this before or after you create the pivot table.

I used "pd.to_numeric()" with "errors='coerce'" because quantity and unit price may have been read as strings or may contain invalid values. Converting them to numeric values makes sure that the multiplication used to calculate sales works correctly. Invalid values become missing values instead of causing the program to fail. I used "np.sum" because NumPy functions are designed to work efficiently with arrays and Pandas data, especially when the dataset is large. Setting "display.max_columns" to "None" tells Pandas to display every column instead of hiding some columns in the middle. I can set this option before or after creating the pivot table because it only changes how the dataframe is displayed, not how the pivot table is calculated.


Add to the program you created in 2 by adding in sub-columns showing the average sales by state and by sale type (retail or wholesale). Set the Panda option to format the output with only 2 decimals using  "display.float_format", "${:,.2f}".format
Hint: this is a very small addition to the aggfunc addition parameter.

I added "np.mean" to the "aggfunc" parameter so the pivot table could show the average sales in addition to the total sales. The averages can be separated by state and by order type, which gives more detail than only looking at the overall totals. I set "display.float_format" to ""${:,.2f}".format" so that the sales values would display as dollar amounts with commas and two decimal places. This only changes the presentation of the results and does not change the actual calculations.


[on your own] From an MIS perspective:
Discuss the advantages and disadvantages of using pivot tables in Python versus Excel. Hint: discuss dealing with a large dataset, user error, consistency of analytics, flexibility in analytics, structured analytics applications versus unstructured analytics 

Using pivot tables in Python is useful when the dataset is large because Python can repeat the same calculations without requiring me to manually select the data each time. Python also reduces user error because the steps are written in a program and can be run again consistently. It is flexible because I can combine the pivot table with other data cleaning and analysis. However, Excel can be easier for users who are more comfortable with clicking and dragging in a spreadsheet. Python also requires programming knowledge.


Explain the advantages of using a dataset “in the cloud” rather than downloading the file and using it locally.

Using a dataset in the cloud means that I can access the most current version of the data without downloading another copy every time it changes. It also saves local storage and makes it easier for multiple people or programs to use the same source. A disadvantage is that the program depends on an internet connection and the file permissions or URL could change. For this reason, I would still use exception handling and check that the data was loaded correctly.

Explain why you would want to use numpy math functions (e.g. np.sum, no.mean) rather than Python built-in functions or creating custom functions. Hint: dealing with a large dataset

I would use NumPy math functions because they are designed to perform calculations on arrays and work efficiently with large amounts of data. They work well with Pandas functions such as pivot tables and groupby operations. Using an existing NumPy function is usually less error-prone and more consistent than writing my own custom function. Python built-in functions can work for simple values, but NumPy functions are better suited for numerical datasets.


What does “defensive programming” mean and give examples of it from these lab exercises. Explain why this is important.

Defensive programming means writing code that anticipates possible errors and responds to them instead of assuming that every input will be perfect. Examples from these labs include using "try/except" when reading the CSV file, skipping bad lines, using "pd.to_numeric()" with "errors='coerce'", and converting the date column with Pandas. These steps are important because a large dataset can contain missing, invalid, or incorrectly formatted values. Defensive programming helps the program continue running and makes the results more reliable.


Give some strategies for assuring (checking) that the calculations and presentation of the pivot table are correct. Keep in mind that this is a large data set!

I would first check the dataframe dimensions, column names, data types, and first few rows after reading the file. I would check for missing or invalid values in quantity, unit price, order date, and sales before creating the pivot table. I could calculate a small sample of sales by hand and compare it with the sales column. I would also compare the pivot table margins with the total of the sales column and check that the Retail and Wholesale columns add up to the totals. 

Note: If you use AI in answering the above questions, do not simply copy the answers you get! The answers AI gives tend to be overly general, verbose, and often not complete. You must carefully review and edit the answers you get from AI!
