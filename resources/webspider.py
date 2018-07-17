

import urllib
import requests
from bs4 import BeautifulSoup

theurl = "https://twitter.com/realdonaldtrump"
thepage =  requests.get(theurl).text

soup = BeautifulSoup(thepage,"html.parser")

print(soup.title.text)
for link in soup.findAll('a'):
    print(link.get('href'))

i=1
for tweets in soup.findAll('div',{"class":"content"}):
    print(i)
    print(tweets.find('p').text)
    i+=1
    
    