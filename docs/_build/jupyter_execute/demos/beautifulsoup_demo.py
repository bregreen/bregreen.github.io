# Scraping Counter-Currents
    Note: This has been edited to scrape the website in small batches. You can't run this freely without making changes.

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

### Call the Main page of interest - Counter Currents
mainpageURL = 'https://counter-currents.com'
page = requests.get(mainpageURL)

## Check Page Pull Success
def PageSuccess(page):
    if page.status_code == 200:
        print('Success!')
    else:
        print("Page error occured.")

PageSuccess(page)

## Run Beautiful Soup on Main page

soup = BeautifulSoup(page.content, 'html.parser')

## Pulling URLs for archives section into list
archives = soup.find(id="archives-2")
#print(archives.prettify())
archive_months = archives.find_all('li')


## How many months of archives did I pull?

print("How many months worth of archives did I pull?: ", len(archive_months), '\n', "Years: ", len(archive_months)/12)
#display(archive_months)


## For each month in archive, pull link into list and provide details if wanted/needed

archive_url_list = []

for a_month in archive_months:
    link = a_month.find('a')['href']
    archive_url_list.append(link)
    

print("Does this count match the above month count?: ", len(archive_url_list)==len(archive_months))

## For each article in the archive month list, get url


article_url_list_ = []

for URL in archive_url_list:
    soup2 = BeautifulSoup(requests.get(URL).content, 'html.parser')
    articles = soup2.find_all('h2', class_="entry-title")
    for art in articles:
        link_a = art.find('a')['href']
        article_url_list_.append(link_a)  



## How many article urls did I pull?

print("How many article urls did I pull?: ", len(article_url_list_), '\n'*2, article_url_list_[:3])

from datetime import date

today = str(date.today())
print("Today's date:", today)

# Save URL list so I don't repeat
#a_urllist = pd.DataFrame(article_url_list_)
#a_urllist.to_csv(r'urllist' + today + '.csv', index=False) 


# Holder/Dictionary
text_data = {}


# Batch Pulls
for URL in article_url_list_[1999:2025]:
    url = URL
    soup3 = BeautifulSoup(requests.get(URL).content, 'html.parser')
    if soup3.find('h1', class_="entry-title").text != None:
        title = soup3.find('h1', class_="entry-title").text
    else:
        title = 'NONE' + str(url) 
    title2 = soup3.title.text
    text = soup3.find('div', class_="entry-content").text
    author = soup3.find('span', class_='author vcard').text
    articledeets = soup3.find('div', class_="entry-utility")
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
    text_data[title] = {}
    text_data[title]['url'] = url
    text_data[title]['author'] = author
    text_data[title]['ext_title'] = title2
    text_data[title]['content'] = text
    text_data[title]['pubdate'] = pubdate
    text_data[title]['pubbed_in'] = origpubtag
    text_data[title]['other_tags'] = tagslist

    

# Batch Pulls
for URL in article_url_list_[2025:2225]:
    url = URL
    soup3 = BeautifulSoup(requests.get(URL).content, 'html.parser')
    if soup3.find('h1', class_="entry-title").text != None:
        title = soup3.find('h1', class_="entry-title").text
    else:
        title = 'NONE' + str(url) 
    title2 = soup3.title.text
    text = soup3.find('div', class_="entry-content").text
    author = soup3.find('span', class_='author vcard').text
    articledeets = soup3.find('div', class_="entry-utility")
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
    text_data[title] = {}
    text_data[title]['url'] = url
    text_data[title]['author'] = author
    text_data[title]['ext_title'] = title2
    text_data[title]['content'] = text
    text_data[title]['pubdate'] = pubdate
    text_data[title]['pubbed_in'] = origpubtag
    text_data[title]['other_tags'] = tagslist

a_text = pd.DataFrame(text_data).T


#pulled at date save to txt & csv
a_text.to_csv(r'CounterCurrentsDatapulledtt_' + today + '.txt')
a_text.to_csv(r'CounterCurrentsDatapulledtt_' + today + '.csv')

print(len(a_text['url'].values))

a_text2 = pd.DataFrame(text_data).T


#pulled at date save to txt & csv
a_text2.to_csv(r'CounterCurrentsDatapulledtttt_' + today + '.txt')
a_text2.to_csv(r'CounterCurrentsDatapulledtttt_' + today + '.csv')

print(len(a_text2['url'].values))

pd.set_option('display.max_rows', None)
#val = text_data
#display(val)
display(a_text2.head())



