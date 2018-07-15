from bs4 import BeautifulSoup
import requests

## Passing html object:
with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
    
## Print html object with indentation:     
# print(soup.prettify())    

## Parse title tag
match = soup.title
print(match)

## Remove Tags
match_text = soup.title.text
print(match_text)

## Find div in footer
match_div = soup.find('div', class_="footer")
print(match_div)


## Selective finding
# article = soup.find('div', class_='article')
# print(article)

# headline = article.h2.a.text
# print(headline)

# summary = article.p.text
# print(summary)

## Find All

for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)
    print()