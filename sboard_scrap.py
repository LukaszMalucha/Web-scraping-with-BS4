from bs4 import BeautifulSoup
import requests
import datetime
import nltk
import csv
from nltk.stem import WordNetLemmatizer

######################################################################### PREREQUISITES ##########################################################################################

## DATETIME FORMAT:
datetime_format = '%d/%m/%Y'

## STOPWORDS FILE:
stopwords = set(w.rstrip() for w in open('stopwords.txt'))

## WORD TOKENIZER
def my_tokenizer(s):
    s = s.lower()  
    tokens = nltk.tokenize.word_tokenize(s)
    tokens = [t for t in tokens if len(t) > 2]
    tokens = [t for t in tokens if t not in stopwords] 
    return tokens
    
    
    
## LOAD WEBPAGE    
source = requests.get('http://springboardcourses.ie/results?keywords=&course_levels%5B%5D=UG&methods%5B%5D=1&perPage=50').text


## Pass source to beautifulsoup:
soup = BeautifulSoup(source, 'lxml')

## CSV file
csv_file = open('springboard_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['title', 'provider', 'award', 'ects_credits', 'mode', 'deadline', 'start_date', 'end_date', 'nfq', 'ote_flag', 'skill_area', 'link'])


for course_div in soup.find_all('div', class_="panel panel-primary"):
    
    try:
        # Course Title
        title_div = course_div.find('div', class_="panel-heading").h3.text
        
        ######### FIRST ROW #####################
        
        first_row = course_div.find('div', class_="panel-body")

        # Provider:
        provider = first_row.find('div', class_="col-md-12").p
        provider = str(provider).split('</strong>')[1]
        provider = provider.split('<')[0]
        
        # Award:
        award = first_row.find('div', class_="col-md-5").p
        award = str(award).split('</strong>')[1]
        award = award.split('<')[0]
        
        # ECTS credits:
        credits = first_row.find('div', class_="col-md-3")
        credits = str(credits).split('</strong> ')[1]
        credits = credits.split('<')[0]
        
        ## SECOND CONTENT ROW #############################

        second_row = first_row.find_all('div', "row")[2]
        
        # Mode:
        mode = second_row.find('div', class_="col-md-5")
        mode = str(mode).split('</strong> ')[1]
        mode = mode.split('<')[0]
       
        
        # Application Deadline:
        deadline = second_row.find('div', class_="col-md-4")
        deadline = str(deadline).split('</strong>')[1]
        deadline = deadline.split('<')[0]
        # deadline = datetime.datetime.strptime(deadline, datetime_format)
        # deadline = deadline.date()
        
        # Start Date
        start_date = second_row.find('div', class_="col-md-3")
        start_date = str(start_date).split('</strong>')[1]
        start_date = start_date.split('<')[0]
        # start_date = datetime.datetime.strptime(start_date, datetime_format)
        # start_date = start_date.date()
        
        # End Date
        end_date = second_row.find('div', class_="col-md-3")
        end_date = str(end_date).split('</strong>')[2]
        end_date = end_date.replace(" ", "")
        end_date = end_date.split('<')[0]
        # end_date = datetime.datetime.strptime(end_date, datetime_format)
        # end_date = end_date.date()
        
        #### BOTTOM ROW ####################

        third_row = first_row.find('div', "row margin-bottom-0")
        
        # NFQ
        nfq = third_row.find('div', class_="col-md-5").p
        nfq = str(nfq).split('</strong>')[1]
        nfq = nfq.split('<')[0]
        
        # Open to those in employment
        ote_flag = third_row.find('div', class_="col-md-4").p
        ote_flag = str(ote_flag).split('</strong>')[1]
        ote_flag = ote_flag.split('<')[0]
        
        # Skills area
        skill_list = third_row.find('div', class_="col-md-3")
        skill_list = str(skill_list).split('</strong>')[1]
        skill_list = skill_list.split('<')[0]
        # skill_list = my_tokenizer(skill_list)
        
        ##### LINK ##############################
        link = course_div.find('a')
        link = link.get('href')
        
    except Exception as e:
        
        title_div = None
        provider = None
        award = None
        credits = None
        mode = None
        deadline = None
        start_date = None
        end_date = None
        nfq = None
        ote_flag = None
        skill_list = None
        link = None
    
    
    
    print(title_div)
    print(provider)
    print(award)
    print(credits)
    print(mode)
    print(deadline)
    print(start_date)
    print(end_date)
    print(nfq)
    print(ote_flag)
    print (skill_list)
    print (link)
    
    print()
    
    csv_writer.writerow([ title_div ,  provider ,  award ,  credits ,  mode ,  deadline ,  start_date ,  end_date ,  nfq ,  ote_flag ,  skill_list ,  link ])
    

csv_file.close()    


