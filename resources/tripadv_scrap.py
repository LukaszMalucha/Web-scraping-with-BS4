import os
import urllib
import requests
from bs4 import BeautifulSoup
from string import ascii_lowercase

def make_soup(url):
    thepage = requests.get(url).text
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata
    
soup = make_soup("https://www.tripadvisor.ie/Hotel_Review-g46863-d114488-Reviews-or-Clinton_Inn_Hotel_Event_Center-Tenafly_New_Jersey.html")

review = soup.find(attrs={"class":"entry"}).text

print(review)






# https://www.tripadvisor.ie/Hotel_Review-g46863-d114488-Reviews-or-Clinton_Inn_Hotel_Event_Center-Tenafly_New_Jersey.html
# https://www.tripadvisor.ie/Hotel_Review-g46863-d114488-Reviews-or5-Clinton_Inn_Hotel_Event_Center-Tenafly_New_Jersey.html
# https://www.tripadvisor.ie/Hotel_Review-g46863-d114488-Reviews-or10-Clinton_Inn_Hotel_Event_Center-Tenafly_New_Jersey.html
# https://www.tripadvisor.ie/Hotel_Review-g46863-d114488-Reviews-or15-Clinton_Inn_Hotel_Event_Center-Tenafly_New_Jersey.html
# https://www.tripadvisor.ie/Hotel_Review-g46863-d114488-Reviews-or295-Clinton_Inn_Hotel_Event_Center-Tenafly_New_Jersey.html