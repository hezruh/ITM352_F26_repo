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