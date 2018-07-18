import os
import urllib
import requests
from bs4 import BeautifulSoup


def make_soup(url):
    thepage = requests.get(url).text
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata
    
    
### PRINT DATA OUT OF TABLE    
    
playerdatasaved=""

soup = make_soup("http://www.basketball-reference.com/players/a/")

for record in soup.findAll('tr'):
    playerdata=""
    for data in record.findAll('td'):
        playerdata=playerdata+","+data.text
    if len(playerdata) !=0:                                                     ## avoid double empty row    
        playerdatasaved = playerdatasaved + "\n" + playerdata[1:]  
   
header="Player,From,To,Pos,Ht,Wt,Birth Date,College" 
file = open(os.path.expanduser("Baketball.csv"), "wb")
file.write(bytes(header, encoding="ascii", errors='ignore'))
file.write(bytes(playerdatasaved, encoding="ascii", errors='ignore'))
print(playerdatasaved)    

