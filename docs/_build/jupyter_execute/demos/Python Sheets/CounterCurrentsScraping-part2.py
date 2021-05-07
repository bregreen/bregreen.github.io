# Scraping Counter-Currents

# Imports

from   collections import Counter
import numpy as np
import os
import random
import requests
import spacy
from collections import defaultdict
import string 
import pandas as pd
from bs4 import BeautifulSoup
from glob import glob
import statsmodels.stats.api as sms
from scipy import stats

import csv

article_url_list_ = []

with open('urllist2020-11-29.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        article_url_list_.append(row)
        


flat_list = [item for sublist in article_url_list_ for item in sublist]

from datetime import date

today = str(date.today())
print("Today's date:", today)

def PageSuccess(page):
    if page.status_code == 200:
        print('Success!')
    else:
        print("Page error occured.")

print(flat_list[:15])

for URL in flat_list[1:10]:
    soup3 = BeautifulSoup(requests.get(str()"'"+ URL+ "'").content, 'html.parser')
    PageSuccess(soup3)

# Holder/Dictionary
text_data2 = {}

#Batch2

for URL in flat_list[1999:2500]:
    url = URL
    soup3 = BeautifulSoup(requests.get(str(URL)).content, 'html.parser')
    if soup3.find('h1', class_="entry-title").text != None:
        title = soup3.find('h1', class_="entry-title").text
    else:
        title = 'NONE' + str(url)
    title2 = soup3.title.text
    text = soup3.find('div', class_="entry-content").text
    author = 'IDK'
    checkauthor = soup3.find('span', class_='author vcard')
    if checkauthor != None:
        author = checkauthor
    else:
        pass
    if soup3.find('div', class_="entry-utility").find('span', class_='entry-date date updated').text != None:
        pubdate = soup3.find('div', class_="entry-utility").find('span', class_='entry-date date updated').text
    else:
        pubdate = 'NONE'
    if soup3.find('div', class_="entry-utility").find('span', class_='cat-links').text != None:
        origpubtag = soup3.find('div', class_="entry-utility").find('span', class_='cat-links').text
    else:
        origpubtag = 'None'
    if soup3.find('div', class_="entry-utility").find('span', class_='tag-links') != None:
        taglinks = soup3.find('div', class_="entry-utility").find('span', class_='tag-links')
    else:
        taglinks = 'None'
    tagslist = []
    if taglinks != 'None':
        tags = taglinks.find_all('a')
        for link in tags:
            addtag = link.get_text()
            tagslist.append(addtag)
    else:
        tagslist.append('NONE')
    text_data2[title] = {}
    text_data2[title]['url'] = url
    text_data2[title]['author'] = author
    text_data2[title]['ext_title'] = title2
    text_data2[title]['content'] = text
    text_data2[title]['pubdate'] = pubdate
    text_data2[title]['pubbed_in'] = origpubtag
    text_data2[title]['other_tags'] = tagslist


for URL in flat_list[2500:3000]:
    url = URL
    soup3 = BeautifulSoup(requests.get(str(URL)).content, 'html.parser')
    if soup3.find('h1', class_="entry-title").text != None:
        title = soup3.find('h1', class_="entry-title").text
    else:
        title = 'NONE' + str(url)
    title2 = soup3.title.text
    text = soup3.find('div', class_="entry-content").text
    author = 'IDK'
    checkauthor = soup3.find('span', class_='author vcard')
    if checkauthor != None:
        author = checkauthor
    else:
        pass
    pubdate = soup3.find('div', class_="entry-utility").find('span', class_='entry-date date updated').text
    origpubtag = soup3.find('div', class_="entry-utility").find('span', class_='cat-links').text
    taglinks = soup3.find('div', class_="entry-utility").find('span', class_='tag-links')
    tagslist = []
    if taglinks != None:
        tags = taglinks.find_all('a')
        for link in tags:
            addtag = link.get_text()
            tagslist.append(addtag)
    else:
        tagslist.append('NONE')
    text_data2[title] = {}
    text_data2[title]['url'] = url
    text_data2[title]['author'] = author
    text_data2[title]['ext_title'] = title2
    text_data2[title]['content'] = text
    text_data2[title]['pubdate'] = pubdate
    text_data2[title]['pubbed_in'] = origpubtag
    text_data2[title]['other_tags'] = tagslist

for URL in article_url_list_[3000:3500]:
    url = URL
    soup3 = BeautifulSoup(requests.get(str(URL)).content, 'html.parser')
    if soup3.find('h1', class_="entry-title").text != None:
        title = soup3.find('h1', class_="entry-title").text
    else:
        title = 'NONE' + str(url)
    title2 = soup3.title.text
    text = soup3.find('div', class_="entry-content").text
    author = 'IDK'
    checkauthor = soup3.find('span', class_='author vcard')
    if checkauthor != None:
        author = checkauthor
    else:
        pass
    pubdate = soup3.find('div', class_="entry-utility").find('span', class_='entry-date date updated').text
    origpubtag = soup3.find('div', class_="entry-utility").find('span', class_='cat-links').text
    taglinks = soup3.find('div', class_="entry-utility").find('span', class_='tag-links')
    tagslist = []
    if taglinks != None:
        tags = taglinks.find_all('a')
        for link in tags:
            addtag = link.get_text()
            tagslist.append(addtag)
    else:
        tagslist.append('NONE')
    text_data2[title] = {}
    text_data2[title]['url'] = url
    text_data2[title]['author'] = author
    text_data2[title]['ext_title'] = title2
    text_data2[title]['content'] = text
    text_data2[title]['pubdate'] = pubdate
    text_data2[title]['pubbed_in'] = origpubtag
    text_data2[title]['other_tags'] = tagslist

for URL in article_url_list_[3500:]:
    url = URL
    soup3 = BeautifulSoup(requests.get(str(URL)).content, 'html.parser')
    if soup3.find('h1', class_="entry-title").text != None:
        title = soup3.find('h1', class_="entry-title").text
    else:
        title = 'NONE' + str(url)
    title2 = soup3.title.text
    text = soup3.find('div', class_="entry-content").text
    author = 'IDK'
    checkauthor = soup3.find('span', class_='author vcard')
    if checkauthor != None:
        author = checkauthor
    else:
        pass
    pubdate = soup3.find('div', class_="entry-utility").find('span', class_='entry-date date updated').text
    origpubtag = soup3.find('div', class_="entry-utility").find('span', class_='cat-links').text
    taglinks = soup3.find('div', class_="entry-utility").find('span', class_='tag-links')
    tagslist = []
    if taglinks != None:
        tags = taglinks.find_all('a')
        for link in tags:
            addtag = link.get_text()
            tagslist.append(addtag)
    else:
        tagslist.append('NONE')
    text_data2[title] = {}
    text_data2[title]['url'] = url
    text_data2[title]['author'] = author
    text_data2[title]['ext_title'] = title2
    text_data2[title]['content'] = text
    text_data2[title]['pubdate'] = pubdate
    text_data2[title]['pubbed_in'] = origpubtag
    text_data2[title]['other_tags'] = tagslist

a_text2 = pd.DataFrame(text_data2).T

#pulled at date save to txt & csv
a_text2.to_csv(r'CounterCurrentsData2pulled_' + today + '.txt')
a_text2.to_csv(r'CounterCurrentsData2pulled_' + today + '.csv')


print(len(text_data2['url'].values))

pd.set_option('display.max_rows', None)
display(text_data2.head())

text_data2.to_pickle(r'CC_all_pickle2' + today + '.pkl')

