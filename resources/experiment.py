import pandas as pd
import numpy as np
import datetime
import nltk

dataset = pd.read_csv('springboard_scrape.csv')

dataset = dataset.dropna()

skill = "Engineering, manufacturing and construction"
skills = []

for row in dataset['skill_area']:
        for skill in row:
                skills.append(skill)
                
                
                
                
def my_tokenizer(skill):
    s = s.lower()  
    tokens = nltk.tokenize.word_tokenize(s)
    tokens = [t for t in tokens if len(t) > 2]
    tokens = [t for t in tokens if t not in stopwords] 
    return tokens                