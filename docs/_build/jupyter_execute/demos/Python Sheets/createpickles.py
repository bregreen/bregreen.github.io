# Counter-Currents Articles

I'm working with a set of about 3,000 short text documents from the Counter-Currents, a white nationalist website. 

I need to perform some preprocessing, then vectorize the documents.

Note that the file with which we're working collects all the records into a single document. Individual cases are delimited with two newlines, hence we split on '\n\n'.

#Imports 

%matplotlib inline
import sys
from   collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import os
import random
import requests
import seaborn as sns
from nltk import word_tokenize, sent_tokenize
from sklearn.datasets import make_blobs
import spacy
from collections import defaultdict
import string 
import pandas as pd
from glob import glob
from scipy import stats
import re
import csv


print(sys.version)

#################################

from datetime import date

today = date.today()
print("Today's date:", today)

blogrows = []

with open('blogtext.csv') as f:
    reader = csv.DictReader(f)
    #for row in reader: (if everything worked, this would have worked!)
    done = False
    while not done:
        try:
            row = next(reader)
            if len(row["text"].split())>100:
                blogrows.append(row)
        except Exception as e:
            if str(e) == '':
                done = True

blogtext_df = pd.DataFrame(blogrows)
blogtext_df['text'] = blogtext_df['text'].str.lower()
blogtext_df['publication'] = 'blogtext'
blogtext_df.head()

len(blogtext_df.values)

newsrows = []

outlets =['CNN', 'Fox']

with open('all-the-news-2-1.csv') as f:
    reader = csv.DictReader(f)
    #for row in reader: (if everything worked, this would have worked!)
    done = False
    while not done:
        try:
            row = next(reader)
            if len(row["article"].split())>100 and (outlets[0] in row["publication"] or outlets[1] in row["publication"]):
                newsrows.append(row)
        except Exception as e:
            if str(e) == '':
                done = True

newstext_df = pd.DataFrame(newsrows)
newstext_df['text'] = newstext_df['article'].str.lower()
newstext_df.head()

len(newstext_df.values)

bb_rows = []


with open('newsbb.csv') as f:
    reader = csv.DictReader(f)
    #for row in reader: (if everything worked, this would have worked!)
    done = False
    while not done:
        try:
            row = next(reader)
            if len(row["content"].split())>100 and ('Breitbart' in row["publication"]):
                bb_rows.append(row)
        except Exception as e:
            if str(e) == '':
                done = True

breit_df = pd.DataFrame(bb_rows)
breit_df['text'] = breit_df['content'].str.lower()
display(breit_df.head())
print(len(breit_df.values))

CCp1 = pd.read_csv('CounterCurrentsDatapulledtttt_2020-11-30.csv', index_col=0)

CCp1.head()

CCp2 = pd.read_csv('CounterCurrentsDatapulled_2020-11-29_1.csv', index_col=0)

CCp2.head()

combo = [CCp1, CCp2]
CC_data = pd.concat(combo)
CC_data['publication']= 'CounterCurrents'
CC_data['text']= CC_data['content'].str.lower()

print(len(CC_data['url'].values))

blogtext_df.to_pickle(r'blogtext_data.pkl')
newstext_df.to_pickle(r'newstext_data.pkl')
breit_df.to_pickle(r'breit_data.pkl')
CC_data.to_pickle(r'CC_data.pkl')