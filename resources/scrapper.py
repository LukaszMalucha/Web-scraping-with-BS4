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

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv.writer.writerow(['headline', 'summary', 'video_link'])

for article in soup.find_all('article'):

    
    yt_link = f'https://youtube.com/watch?v={vid_id}'
    print(yt_link)
    
    try:
        
        vid_src = article.find('iframe', class_ = 'youtube-player')['src']
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]
    except Exception as e:
        yt_link = None
        
    print(yt_link)    
    
    print()
    
    csv_writer.writerow([headline, summary, yt_link])
    
csv_file.close()    