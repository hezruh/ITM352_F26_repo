Lab: OBTAINING DATA FROM THE WEB USING PYTHON 


1. Review the web page at https://data.cityofchicago.org/Historic-Preservation/Landmark-Districts/zidz-sdfj/about_data. Inspect the page to view the HTML. Find and note all the <title> tags. 

Code here:

"""python
# scrape data from city of chicago's data portal
# print any line with a <title> tag in it
import ssl
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://data.cityofchicago.org/Historic-Preservation/Landmark-Districts/zidz-sdfj/about_data"
print("Retrieving", url)

response = urllib.request.urlopen(url)

for line in response:
    line = line.decode("utf-8").strip()
    if "<title>" in line:
        print(line)
"""

The value returned from "urlopen()" is an HTTPResponse object. It represents the response from the web server and can be used like a file, which means that I can iterate through it one line at a time. The SSL context is changed because the website may otherwise return an SSL certificate error when Python tries to verify the website's certificate.

The lines from the URL stream must be decoded because the response is returned as bytes instead of regular Python strings. Decoding the bytes using UTF-8 converts the response into text that Python can search and print.

The title tag found in the page is:

"""html
<title>Landmark Districts | City of Chicago | Data Portal</title>
"""

2. Open the URL url = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202603" and note the table of interest rate data. 

Code here:

"""python
# grab 1 month interest rate from the US treasury website
import ssl, lxml
import pandas as pd
import urllib.request

url = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202603"
print("Retrieving", url)

webpage = urllib.request.urlopen(url)
df = pd.read_html(webpage)
print("Columns:", df[0].columns)

int_rate_table = df[0]

# print the table of 1 month interest rates
print("1 month interest rates:")

for index, row in int_rate_table.iterrows():
    print("Date: ", row["Date"], "1 month rate: ", row["1 Mo"])
"""

The return value from ".read_html()" is a list of DataFrames. The first DataFrame in the list, "df[0]", is the table of interest rate data. Pandas searches the HTML for table tags and converts each table that it finds into a DataFrame. The "lxml" library is used by Pandas to parse the HTML.

3. Inspect the website https://shidler.hawaii.edu/itm/people and note the HTML that displays the people “cards”. Hint: look for the <article> elements 

Code here:

"""python
# scrape names of ITM faculty and graduate students
import ssl
import urllib.request
from bs4 import BeautifulSoup

itm_url = "https://shidler.hawaii.edu/itm/people"
itm_page = urllib.request.urlopen(itm_url)
itm_names = []

soup = BeautifulSoup(itm_page, 'html.parser')

# find all the faculty which are in h2 tags with class = "title"
faculty = soup.find_all('h2', class_='title')

for person in faculty:
    itm_names.append(person.text)
    print("Faculty: ", person.text)
"""

The "BeautifulSoup" object contains the HTML document in a searchable and navigable form. This is useful because it allows me to find specific tags, classes, and attributes without having to manually search through the entire HTML page.

The first few lines of the prettified HTML would look similar to this:

"""html
<!DOCTYPE html>
<html lang="en">
 <head>
  <meta charset="utf-8"/>
  <title>People | Shidler College of Business</title>
"""

The people cards are contained in "<article>" elements. The code above finds the people names by searching for the "<h2>" elements with the "title" class. The number of people found can be printed with "len(faculty)". The first card can be printed with "faculty[0].prettify()", or the article cards can be found with "soup.find_all('article')". The same cards can be searched for email links using an "<a>" tag whose "href" begins with "mailto:".

4. Retrieve and analyze public vehicle license data from Chicago’s open API using sodapy and pandas. 

Code here:

"""python
# get public license data from City of Chicago's data portal
import ssl
import pandas as pd
from sodapy import Socrata

client = Socrata("data.cityofchicago.org", None)

json_file = "rr23-ymwb"

results = client.get(json_file, limit=500)
# convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)
results_df.info()

vehicles = results_df[["public_vehicle_number", "vehicle_fuel_source"]]
print("Public vehicle numbers and fuel sources:")

vehicles.info()
vehicles_by_fuel = vehicles.groupby("vehicle_fuel_source").count()
print(vehicles_by_fuel)
"""

The result from the Socrata API is a list of dictionary records. "DataFrame.from_records()" converts those records into a Pandas DataFrame. The "vehicles" DataFrame selects the public vehicle number and fuel source columns. The "groupby()" method groups the vehicles by fuel source, and "count()" counts the number of vehicles in each group.

5. Use the requests package to create a REST query that returns the count of licenses by driver_type.

Code here:

"""python
# get a JSON file from the City of Chicago's data portal and analyze driver types
import ssl
import pandas as pd
import requests

url = "https://data.cityofchicago.org/resource/97wa-y6ff.json?$select=driver_type,count(license)&$group=driver_type"
response = requests.get(url)

response_json = response.json()
print("Driver types and counts:")
print(response_json)

response_df = pd.DataFrame.from_records(response_json)
response_df.columns = ["driver_type", "count_license"]
response_df = response_df.set_index("driver_type")

print(response_df)
"""

The response from ".json()" is a list of dictionaries. Each dictionary contains a driver type and the count of licenses for that driver type. The list is converted into a DataFrame, the columns are renamed, and "driver_type" is used as the index.

A REST query is a request made to a web service using a URL. The query in this exercise uses the "$select" part to choose the "driver_type" and count of licenses, and it uses "$group=driver_type" to group the results by driver type. The "requests.get()" function sends the query to the API, and the API returns the requested data as JSON.

6. ON YOUR OWN: Use the requests package to retrieve a page of mortgage rate info from the Hawaii Board of Realtors site that lists current local mortgage rates: https://www.hicentral.com/hawaii-mortgage-rates.php 

The page can be retrieved with "requests.get()", and the rate table can be extracted with Pandas:

"""python
import pandas as pd
import requests

url = "https://www.hicentral.com/hawaii-mortgage-rates.php"
response = requests.get(url)
response.raise_for_status()

tables = pd.read_html(response.text)
rates = tables[0]

for index, row in rates.iterrows():
    print(row.to_string())
"""

This returns the mortgage rate table as a DataFrame. Each iteration prints one row, including the name of the bank and its current mortgage rates.
