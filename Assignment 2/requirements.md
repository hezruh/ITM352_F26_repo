Assignment 2: Build a sales dashboard


The goal of this assignment is to create an interactive, text-based dashboard using Pandas pivot tables. The dashboard will allow users to explore and analyze sales data in various dimensions (e.g., by region, employee, product, and customer). The dashboard provides both predefined analytical tasks and custom pivot table exploration to analyze sales data.


In this assignment, you are expected to use proper programming style, using defensive programming, error checking and recovery, and assurance that the application functions as required with high-quality (easy to fix problems, easy to extend, easy to maintain, provably gives correct results). It should be well documented with comments and a simple user guide with examples.  


Requirements
R1. Loading sales data
Use must use the sales data file 'sales_data.csv' from Google Drive at https://drive.google.com/file/d/1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA/view?usp=drive_link  Display indicator that the file is loading and when it was successfully loaded. If unsuccessful, end the program with an appropriate error message. If successful, display time it took to load, how many rows of data, and list the available columns. Replace any missing data with zeros. Check that the data has the required fields for the analytics in the dashboard and warn the user about missing fields and that some analytics may not work. 


R2. Interactive command line menu 
Implement a text-based menu interface that allows the user to interact with the data through a command-line interface with the following menu of basic dashboard functions:


--- Sales Data Dashboard ---
1. Show the first n rows of sales data
2. Total sales by region and order_type
3. Average sales by region with average sales by state and sale type
4. Sales by customer type and order type by state.
5. Total sales quantity and price by region and product
6. Total sales quantity and price customer type
7. Max and min sales price of sales by category
8. Number of unique employees by region
9. Create a custom pivot table
10. Exit


Implement the menu in a general way that enables easy addition, removal, or reordering of menu items by creating a tuple of menu items. A menu item could be a tuple (menu item, item function) or a dictionary {menu item : item function). All menu items should correspond to a custom function that performs the menu task.


R3. Predefined analytical tasks
Include predefined analytical task options that generate pivot tables to the following specific analyses (these correspond to the menu items shown in R2):
Show the first n rows of sales data: Ask the user how many rows of sales data to display starting from the first row. If user does not enter a value, no rows are displayed. If the user selects “all” then all rows are displayed. User should be told how many rows are available and not allow invalid input.


Enter rows to display:
- Enter a number 1 to 5129
- To see all rows, enter 'all'
- To skip preview, press Enter
Your choice: 


Total sales by region and order_type: Create a pivot table aggregating sales by region, with columns defined by order_type (which is either Retail or Wholesale).
Average sales by region with average sales by state and sale type: Create a pivot table aggregating sales by region with sub-columns showing the average sales by state, by sale type (retail or wholesale).
Sales by customer type and order type by state: Create a pivot table with sub-rows showing sales by customer type and order type. Show this by state.
Total sales quantity and price by region and product: Create a pivot table that shows sales by region and product, summing the quantity and sales price per row.
Total sales quantity and price customer type: Create a pivot table that shows sales by order and customer type, summing the quantity and sales price per row.
Max and min sales price of sales by category:  Create a pivot table that shows sales by category, and also shows the max and min sales price per row.
Number of unique employees by region: Create a pivot table that shows the number of employees by region. Count unique employees.


R4. Create custom pivot table
Create a Pivot Table Generator which allows the user to select different dimensions to analyze the sales data. This will be an interactive submenu enabling the user to choose:


Rows: Which field(s) should group the data (e.g., sales_region, employee_name, product_category)


Select rows:
1. employee_name
2. sales_region
3. product_category
Enter the number(s) of your choice(s), separated by commas:


Columns: Optional column grouping (e.g., order_type, customer_type)


Select columns (optional):
1. order_type
2. customer_type
Enter the number(s) of your choice(s), separated by commas (enter for no grouping):


Values: Numeric fields to analyze (e.g., quantity, sale_price)


Select values:
1. quantity
2. sale_price
Enter the number(s) of your choice(s), separated by commas:


Aggregation function: (e.g., sum, mean, count)
Select aggregation function:
1. sum
2. mean
3. count
Enter the number(s) of your choice(s), separated by commas: 


Quality requirements
User Input Validation: Ensure the user inputs are valid (e.g., selecting only available fields).
Documentation: Clear and useful code comments. Explain the design of non-trivial things. Remove unnecessary or trivial comments.
Defensive programming: Anticipate and handle potential problems to ensure the application will not fault given a bad or inaccessible data file, corrupt or bad data, bad inputs, etc. Use assertions as you write the code to help determine where you need error handling.
Style: Follow good naming conventions for variables, functions, and file names. Use custom functions to organize, document, and increase flexibility
User Interface: The menu should be intuitive and should give instructions for inputs, the output should be nicely formatted and easy to read
Testing: You must supply a full set of test cases that cover every function and overall capability.
Maintainability: The dashboard application should be designed to be easily maintained (fixing bugs, adding new analytics). Implement the code in a readable, simple, and straightforward way. Do not try to be efficient or clever.


In the comments of the code, explain any notable things you did to address the above requirements. 


Individual Requirements 
Use the requirements assignment app to get your assignments. You will be assigned two of the above requirements, and you must implement them both. In addition, you may choose to do some of the other requirements for extra credit.


For each result, ask the user if they want the results exported to an Excel file (that can be read directly into Excel). Ask the user what filename they want.
When the sales data is loaded, display a summary of the data (total orders, number of employees, sales regions, dates range of orders, number of unique customers, product categories, unique states, total sales amount, total quantities of products sold). If some data is not available (missing columns) for a pre-defined analytic, remove that analytic from the menu options.
Create an alternate data set. Allow the user to select what sales data to load. 
Enable the user to get two analytics results and compare them side by side. Hint: return the pivot table from the function rather than just printing it out.
Implement a new non-trivial sales analytic (simple variations of existing analytics would not satisfy this requirement). 
For each analytic, ask the user what data rows to use for the analytic (a range or a list of rows). Use only this data for the analysis.
Before performing an analysis, ask the user what date range of sales data to use. Use only that range for the analysis.
Add an analytic that shows sales by region and product, showing the percentage of the quantity and total sales per region and product.  This percentage should be a new column in the pivot table.
Instead of replacing missing data in the pivot table with zeroes, replace it with the mean value for that column.  
Keep track of which analytics have been done and store the results. List them above the menu. Add a menu item that displays all the stored results. Determine a useful way to handle saving custom pivot tables created. Hint: create an empty dictionary at the start of the application. Whenever you get a pivot table, add it to this dictionary. 




NOTES about use of AI: 
You are encouraged to use AI to help you with this assignment (Claude is a good choice). If you use AI-generated code, you are required to do the following:
You must specify where and how you used AI in your code comments e.g. “This function was generated using ChatGPT with the prompt …”
You must provide adequate comments in the code. AI-generated code tends to provide too detailed comments about what specific code does and not what the code does for the overall application.
You must ensure that the code you use meets the requirements for the assignment. 
Never not use generated code that you do not fully understand. AI may utilize more advanced programming concepts and things we did not discuss in class. Either adapt the code to what you fully understand or don’t use it.

There is no penalty for using AI. However, failing to follow the above guidelines will result in point deductions. If you use AI just for reference and examples you do not need to do the above. You are discouraged from attempting to get AI to build the entire application. You are likely to get better results if you use AI to help incrementally with small parts, giving specific guidance and testing along the way rather than a “one shot” agent driven development.
