import pandas as pd
import numpy as np
import datetime

dataset = pd.read_csv('springboard_scrape.csv')

dataset = dataset.dropna()

datetime_format = '%d/%m/%Y'






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



max_length_skills = dataset['skill_area'].map(len).max()



df_skills = pd.DataFrame(dataset['skill_area'].str.split(',', expand=True).values, columns=['skill_area_1','skill_area_2','skill_area_3','skill_area_4'])

df_skills_1 = []

for element in df_skills['skill_area_1']:
        if element:
                element = element.replace("[","")
                element = element.replace("]","")
                element = element.replace("'","")
                element = element.strip()
                df_skills_1.append(element)
        else:
                pass
        

df_skills['skill_area_1'] = df_skills_1        
  
      
df_skills_2 = []


for element in df_skills['skill_area_2']:
        if element:
                element = element.replace("[","")
                element = element.replace("]","")
                element = element.replace("'","")
                element = element.strip()
                df_skills_2.append(element)
        else:
                pass
        
df_skills['skill_area_2'] = df_skills_2               


df_skills_3 = []

for element in df_skills['skill_area_3']:
        if element:
                element = element.replace("[","")
                element = element.replace("]","")
                element = element.replace("'","")
                element = element.strip()
                df_skills_3.append(element)
        else:
                pass
        
df_skills['skill_area_3'] = df_skills_3               

df_skills_4 = []

for element in df_skills['skill_area_4']:
        if element != None:
                element = element.replace("[","")
                element = element.replace("]","")
                element = element.replace("'","")
                element = element.strip()
#                df_skills_4.append(element)
        else:
                pass
        df_skills_4.append(element)        
                
df_skills['skill_area_4'] = df_skills_4            


        













 