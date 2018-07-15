from bs4 import BeautifulSoup
import requests

## Get response object:

source = requests.get('https://lukaszmalucha.github.io/UCFD-Milestone-Project/').text

## Pass source to beautifulsoup
soup = BeautifulSoup(source, 'lxml')


# print(soup.prettify())

### Grab material icons

body = soup.find('body')
dashboard_cards = body.find('div', class_='dashboard-cards').p.text
print(dashboard_cards)


### Parse youtube link example

vid_src = article.find('iframe', class_ = 'youtube-player')['src']
print(vid_src)

vid_id = vid_src.split('/')[4]
vid_id = vid_id.split('?')[0]
print(vid_id)

yt_link = f'https://youtube.com/watch?v={vid_id}'

for article in soup.find_all('article'):
    vid_src = article.find('iframe', class_ = 'youtube-player')['src']
    print(vid_src)
    
    vid_id = vid_src.split('/')[4]
    vid_id = vid_id.split('?')[0]
    print(vid_id)
    
    yt_link = f'https://youtube.com/watch?v={vid_id}'
    print(yt_link)
    
    print()