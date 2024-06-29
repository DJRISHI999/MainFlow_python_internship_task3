# Extract relevant information such as text,links, or images from web pages.

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

# Extracting all the images from the website
images = soup.find_all('img')

# Extracting all the text from the website
text = soup.get_text()

# Printing the title of the website
print(f'Title of the website: {title}\n')

# Printing all the links from the website
print('Links on the website:')
for link in links:
    print(link.get('href'))

# Printing all the images from the website
print('\nImages on the website:')
for image in images:
    print(image.get('src'))

# Printing all the text from the website
print('\nText on the website:')
print(text)

