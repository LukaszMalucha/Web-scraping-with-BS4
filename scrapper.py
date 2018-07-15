from bs4 import BeautifulSoup
import requests

## Get response object:

source = requests.get('https://lukaszmalucha.github.io/UCFD-Milestone-Project/').text

## Pass source to beautifulsoup
soup = BeautifulSoup(source, 'lxml')


# print(soup.prettify())

### Grab material icons

lists = soup.find('li')

icons = lists.i
print(icons)
