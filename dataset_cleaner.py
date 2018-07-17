import pandas as pd
import numpy as np
import datetime
import nltk
from sklearn.preprocessing import MultiLabelBinarizer


dataset = pd.read_csv('springboard_scrape.csv')


dataset = dataset.dropna()   ## remove empty rows

datetime_format = '%d/%m/%Y'



### Dates cleaning

deadline = []

for date in dataset['deadline']:
        if len(date) < 8:
                date = '01/' + date
        else:
                date = date
        date = datetime.datetime.strptime(date, datetime_format)
        date = date.date()        
        deadline.append(date)    
        
        
dataset['deadline'] = deadline        
                


start_date = []                
  
for date in dataset['start_date']:
        if len(date) < 8:
                date = '01/' + date
        else:
                date = date
        date = datetime.datetime.strptime(date, datetime_format)
        date = date.date()           
        start_date.append(date)  
                         
                
dataset['start_date'] = start_date         



end_date = []

for date in dataset['end_date']:
        if len(date) < 8:
                date = '01/' + date
        else:
                date = date
        date = datetime.datetime.strptime(date, datetime_format)
        date = date.date()           
        end_date.append(date)                   
                
dataset['end_date'] = end_date


### Skill area column cleaning


clean_skills = []
for element in dataset['skill_area']:        
        element = element.replace("[","")
        element = element.replace("]","")
        element = element.replace("'","")
        element = element.strip()
        clean_skills.append(element)


df_skills = pd.DataFrame()
df_skills['skills'] = clean_skills

skill_list = []
for element in df_skills['skills']:
        skills = element.split(',')
        skill_list.append(skills)

skill_area = pd.DataFrame()                
skill_area['skills_list'] = skill_list


### Skill Area featurization 

mlb = MultiLabelBinarizer()

new_array = mlb.fit_transform(skill_area['skills_list'])
skill_classes = list(mlb.classes_)
df_skills_transformed = pd.DataFrame(data=new_array, columns=skill_classes)


### Concating two dataframes

frames = [dataset, df_skills_transformed]

dataset_clean = pd.concat(frames, axis = 1)

dataset_clean = dataset_clean.drop(['skill_area'], axis = 1)


### Print to CSV

dataset_clean.to_csv('springboard_clean.csv', index=False)




 