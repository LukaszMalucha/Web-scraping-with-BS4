from bs4 import BeautifulSoup
import requests


source = requests.get('http://springboardcourses.ie/results?keywords=&course_levels%5B%5D=UG&methods%5B%5D=1&perPage=50').text


## Pass source to beautifulsoup:
soup = BeautifulSoup(source, 'lxml')


## See the result:
# print(soup.prettify())


## Find course divs:
course_div = soup.find('div', class_="panel panel-primary")
# print(course_div)

# Course Title
title_div = course_div.find('div', class_="panel-heading").h3.text
print(title_div)

# Course Content
body_div = course_div.find('div', class_="panel-body")

# Provider:
provider = body_div.find('div', class_="col-md-12").p
provider = str(provider).split('</strong>')[1]
provider = provider.split('<')[0]
print(provider)
 
# Award:
award = body_div.find('div', class_="col-md-5").p
award = str(award).split('</strong>')[1]
award = award.split('<')[0]
print(award)

# ECTS credits:
credits = body_div.find('div', class_="col-md-3")
credits = str(credits).split('</strong> ')[1]
credits = credits.split('<')[0]
print(credits)

# Mode:
second_row = body_div.find_all('div', "row")[2]
mode = second_row.find('div', class_="col-md-5")
print(mode)




















