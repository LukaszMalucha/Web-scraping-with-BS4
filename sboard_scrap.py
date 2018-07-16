from bs4 import BeautifulSoup
import requests
import datetime


datetime_format = '%d/%m/%Y'

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

######### FIRST ROW #####################

first_row = course_div.find('div', class_="panel-body")

# Provider:
provider = first_row.find('div', class_="col-md-12").p
provider = str(provider).split('</strong>')[1]
provider = provider.split('<')[0]
print(provider)
 
# Award:
award = first_row.find('div', class_="col-md-5").p
award = str(award).split('</strong>')[1]
award = award.split('<')[0]
print(award)

# ECTS credits:
credits = first_row.find('div', class_="col-md-3")
credits = str(credits).split('</strong> ')[1]
credits = credits.split('<')[0]
print(credits)


## SECOND CONTENT ROW #############################

second_row = first_row.find_all('div', "row")[2]

# Mode:
mode = second_row.find('div', class_="col-md-5")
mode = str(mode).split('</strong> ')[1]
mode = mode.split('<')[0]
print(mode)

# Application Deadline:
deadline = second_row.find('div', class_="col-md-4")
deadline = str(deadline).split('</strong>')[1]
deadline = deadline.split('<')[0]
deadline = datetime.datetime.strptime(deadline, datetime_format)
deadline = deadline.date()
print(deadline)

# Start Date

start_date = second_row.find('div', class_="col-md-3")
start_date = str(start_date).split('</strong>')[1]
start_date = start_date.split('<')[0]
start_date = datetime.datetime.strptime(start_date, datetime_format)
start_date = start_date.date()
print(start_date)

# End Date

end_date = second_row.find('div', class_="col-md-3")
end_date = str(end_date).split('</strong>')[2]
end_date = end_date.replace(" ", "")
end_date = end_date.split('<')[0]
end_date = datetime.datetime.strptime(end_date, datetime_format)
end_date = end_date.date()
print(end_date)


#### BOTTOM ROW ####################

third_row = first_row.find('div', "row margin-bottom-0")

# NFQ

nfq = third_row.find('div', class_="col-md-5").p
nfq = str(nfq).split('</strong>')[1]
nfq = nfq.split('<')[0]

print(nfq)

# Open to those in employment

ote_flag = third_row.find('div', class_="col-md-4").p
ote_flag = str(ote_flag).split('</strong>')[1]
ote_flag = ote_flag.split('<')[0]
print(ote_flag)

# Skills area

skill_list = third_row.find('div', class_="col-md-3")
skill_list = str(skill_list).split('</strong>')
skill_list = 
print (skill_list)








