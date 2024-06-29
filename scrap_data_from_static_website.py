# Develop a simple Python script to scrape data from a static web page.

# Importing the required libraries
from bs4 import BeautifulSoup
import requests

# URL of the website
url = input('Enter the URL of the website: ')

# Sending a request to the website
response = requests.get(url)

# Parsing the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Extracting the title of the website
title = soup.title.string

# Extracting all the links from the website
links = soup.find_all('a')

# Printing the title of the website
print(f'Title of the website: {title}\n')

# Printing all the links from the website

print('Links on the website:')
for link in links:
    print(link.get('href'))
