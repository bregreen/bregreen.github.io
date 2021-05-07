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
a_urllist = pd.DataFrame(article_url_list_)
a_urllist.to_csv(r'urllist' + today + '.csv', index=False) 


text_data = {}

for URL in article_url_list_[:5]:
    url = URL
    soup3 = BeautifulSoup(requests.get(URL).content, 'html.parser')
    title = soup3.find('h1', class_="entry-title").text
    text = soup3.find('div', class_="entry-content").text
    articledeets = soup3.find('div', class_="entry-utility")
    pubdate = articledeets.find('span', class_='entry-date date updated').text
    origpubtag = articledeets.find('span', class_='cat-links').text
    taglinks = articledeets.find('span', class_='tag-links')
    tags = taglinks.find_all('a')
    tagslist = []
    for link in tags:
        addtag = link.get_text()
        tagslist.append(addtag)
    text_data[title] = {}
    text_data[title]['url'] = url
    text_data[title]['content'] = text
    text_data[title]['pubdate'] = pubdate
    text_data[title]['pubbed_in'] = origpubtag
    text_data[title]['other_tags'] = tagslist

for URL in article_url_list_[5:10]:
    url = URL
    soup3 = BeautifulSoup(requests.get(URL).content, 'html.parser')
    title = soup3.find('h1', class_="entry-title").text
    text = soup3.find('div', class_="entry-content").text
    articledeets = soup3.find('div', class_="entry-utility")
    pubdate = articledeets.find('span', class_='entry-date date updated').text
    origpubtag = articledeets.find('span', class_='cat-links').text
    taglinks = articledeets.find('span', class_='tag-links')
    tags = taglinks.find_all('a')
    tagslist = []
    for link in tags:
        addtag = link.get_text()
        tagslist.append(addtag)
    text_data[title] = {}
    text_data[title]['url'] = url
    text_data[title]['content'] = text
    text_data[title]['pubdate'] = pubdate
    text_data[title]['pubbed_in'] = origpubtag
    text_data[title]['other_tags'] = tagslist

a_text = pd.DataFrame(text_data).T
#a_text['wc_cc'], a_text['editedtext'] = a_text['wc_text_listtuple'].str[0], a_text['wc_text_listtuple'].str[1]

#pulled at date save to txt & csv
a_text.to_csv(r'CounterCurrentsData500_2_pulled_' + today + '.txt')
a_text.to_csv(r'CounterCurrentsData500_2_pulled_' + today + '.csv')


## Text from each article

text_data = {}

for URL in article_url_list_[:500]:
    url = URL
    #sepcomments = 'If you want to support Counter-Currents'
    #sepwc = 'words'
    soup3 = BeautifulSoup(requests.get(URL).content, 'html.parser')
    title = soup3.find('h1', class_="entry-title").text
    text = soup3.find('div', class_="entry-content").text
    title2 = soup3.title.text
    #t2 = text.split(sepcomments, 1)[0]
    #t3 = t2.split(sepwc, 1)
    text_data[title] = {}
    text_data[title]['title2'] = title2
    text_data[title]['url'] = url
    text_data[title]['content'] = text
    #text_data[title]['text_unedited'] = t2
    #text_data[title]['wc_text_listtuple'] = t3

    

text_data2 = {}
for URL in article_url_list_[500:1000]:
    url = URL
    #sepcomments = 'If you want to support Counter-Currents'
    #sepwc = 'words'
    soup3 = BeautifulSoup(requests.get(URL).content, 'html.parser')
    title = soup3.find('h1', class_="entry-title").text
    text = soup3.find('div', class_="entry-content").text
    title2 = soup3.title.text
    #t2 = text.split(sepcomments, 1)[0]
    #t3 = t2.split(sepwc, 1)
    #if (text.find('If you want to support Counter-Currents') != -1): 
    #    nocomments = text.split(sepcomments, 1)[0]
    #else: 
    #    nocomments = text
    text_data[title] = {}
    text_data[title]['title2'] = title2
    text_data[title]['url'] = url
    text_data[title]['content'] = text
    #text_data[title]['text_unedited'] = t2
    #text_data[title]['wc_text_listtuple'] = t3


a_text2 = pd.DataFrame(text_data2).T
#a_text2['wc_cc'], a_text2['editedtext'] = a_text2['wc_text_listtuple'].str[0], a_text2['wc_text_listtuple'].str[1]

#pulled at date save to txt & csv
a_text2.to_csv(r'CounterCurrentsData500_1000_pulled_' + today + '.txt')
a_text2.to_csv(r'CounterCurrentsData500_1000_pulled_' + today + '.csv')

text_data3 = {}
for URL in article_url_list_[1000:1500]:
    url = URL
    #sepcomments = 'If you want to support Counter-Currents'
    #sepwc = 'words'
    soup3 = BeautifulSoup(requests.get(URL).content, 'html.parser')
    title = soup3.find('h1', class_="entry-title").text
    text = soup3.find('div', class_="entry-content").text
    title2 = soup3.title.text
    #t2 = text.split(sepcomments, 1)[0]
    #t3 = t2.split(sepwc, 1)
    #if (text.find('If you want to support Counter-Currents') != -1): 
    #    nocomments = text.split(sepcomments, 1)[0]
    #else: 
    #    nocomments = text
    text_data[title] = {}
    text_data[title]['title2'] = title2
    text_data[title]['url'] = url
    text_data[title]['content'] = text
    #text_data[title]['text_unedited'] = t2
    #text_data[title]['wc_text_listtuple'] = t3


a_text3 = pd.DataFrame(text_data3).T
#a_text3['wc_cc'], a_text3['editedtext'] = a_text3['wc_text_listtuple'].str[0], a_text3['wc_text_listtuple'].str[1]

#pulled at date save to txt & csv
a_text3.to_csv(r'CounterCurrentsData1000_1500_pulled_' + today + '.txt')
a_text3.to_csv(r'CounterCurrentsData1000_1500_pulled_' + today + '.csv')

text_data4 = {}
for URL in article_url_list_[1500:2000]:
    url = URL
    #sepcomments = 'If you want to support Counter-Currents'
    #sepwc = 'words'
    soup3 = BeautifulSoup(requests.get(URL).content, 'html.parser')
    title = soup3.find('h1', class_="entry-title").text
    text = soup3.find('div', class_="entry-content").text
    title2 = soup3.title.text
    #t2 = text.split(sepcomments, 1)[0]
    #t3 = t2.split(sepwc, 1)
    #if (text.find('If you want to support Counter-Currents') != -1): 
    #    nocomments = text.split(sepcomments, 1)[0]
    #else: 
    #    nocomments = text
    text_data[title] = {}
    text_data[title]['title2'] = title2
    text_data[title]['url'] = url
    text_data[title]['content'] = text
    #text_data[title]['text_unedited'] = t2
    #text_data[title]['wc_text_listtuple'] = t3


a_text4 = pd.DataFrame(text_data4).T
#a_text4['wc_cc'], a_text4['editedtext'] = a_text4['wc_text_listtuple'].str[0], a_text4['wc_text_listtuple'].str[1]

#pulled at date save to txt & csv
a_text4.to_csv(r'CounterCurrentsData1500_2000_pulled_' + today + '.txt')
a_text4.to_csv(r'CounterCurrentsData1500_2000_pulled_' + today + '.csv')

text_data5 = {}
for URL in article_url_list_[2000:2500]:
    url = URL
    #sepcomments = 'If you want to support Counter-Currents'
    #sepwc = 'words'
    soup3 = BeautifulSoup(requests.get(URL).content, 'html.parser')
    title = soup3.find('h1', class_="entry-title").text
    text = soup3.find('div', class_="entry-content").text
    title2 = soup3.title.text
    #t2 = text.split(sepcomments, 1)[0]
    #t3 = t2.split(sepwc, 1)
    #if (text.find('If you want to support Counter-Currents') != -1): 
    #    nocomments = text.split(sepcomments, 1)[0]
    #else: 
    #    nocomments = text
    text_data[title] = {}
    text_data[title]['title2'] = title2
    text_data[title]['url'] = url
    text_data[title]['content'] = text
    #text_data[title]['text_unedited'] = t2
    #text_data[title]['wc_text_listtuple'] = t3

a_text5 = pd.DataFrame(text_data5).T
#a_text5['wc_cc'], a_text5['editedtext'] = a_text5['wc_text_listtuple'].str[0], a_text5['wc_text_listtuple'].str[1]

#pulled at date save to txt & csv
a_text5.to_csv(r'CounterCurrentsData2000_2500_pulled_' + today + '.txt')
a_text5.to_csv(r'CounterCurrentsData2000_2500_pulled_' + today + '.csv')

text_data6 = {}
for URL in article_url_list_[2500:3000]:
    url = URL
    #sepcomments = 'If you want to support Counter-Currents'
    #sepwc = 'words'
    soup3 = BeautifulSoup(requests.get(URL).content, 'html.parser')
    title = soup3.find('h1', class_="entry-title").text
    text = soup3.find('div', class_="entry-content").text
    title2 = soup3.title.text
    #t2 = text.split(sepcomments, 1)[0]
    #t3 = t2.split(sepwc, 1)
    #if (text.find('If you want to support Counter-Currents') != -1): 
    #    nocomments = text.split(sepcomments, 1)[0]
    #else: 
    #    nocomments = text
    text_data[title] = {}
    text_data[title]['title2'] = title2
    text_data[title]['url'] = url
    text_data[title]['content'] = text
    #text_data[title]['text_unedited'] = t2
    #text_data[title]['wc_text_listtuple'] = t3

a_text6 = pd.DataFrame(text_data6).T
#a_text6['wc_cc'], a_text6['editedtext'] = a_text6['wc_text_listtuple'].str[0], a_text6['wc_text_listtuple'].str[1]

#pulled at date save to txt & csv
a_text6.to_csv(r'CounterCurrentsData2500_3000_pulled_' + today + '.txt')
a_text6.to_csv(r'CounterCurrentsData2500_3000_pulled_' + today + '.csv')

text_data7 = {}
for URL in article_url_list_[3000:3500]:
    url = URL
    #sepcomments = 'If you want to support Counter-Currents'
    #sepwc = 'words'
    soup3 = BeautifulSoup(requests.get(URL).content, 'html.parser')
    title = soup3.find('h1', class_="entry-title").text
    text = soup3.find('div', class_="entry-content").text
    title2 = soup3.title.text
    #t2 = text.split(sepcomments, 1)[0]
    #t3 = t2.split(sepwc, 1)
    #if (text.find('If you want to support Counter-Currents') != -1): 
    #    nocomments = text.split(sepcomments, 1)[0]
    #else: 
    #    nocomments = text
    text_data[title] = {}
    text_data[title]['title2'] = title2
    text_data[title]['url'] = url
    text_data[title]['content'] = text
    #text_data[title]['text_unedited'] = t2
    #text_data[title]['wc_text_listtuple'] = t3

a_text7 = pd.DataFrame(text_data7).T
#a_text7['wc_cc'], a_text7['editedtext'] = a_text7['wc_text_listtuple'].str[0], a_text7['wc_text_listtuple'].str[1]

#pulled at date save to txt & csv
a_text7.to_csv(r'CounterCurrentsData3000_3500_pulled_' + today + '.txt')
a_text7.to_csv(r'CounterCurrentsData3000_3500_pulled_' + today + '.csv')

text_data8 = {}
for URL in article_url_list_[3500:]:
    url = URL
    #sepcomments = 'If you want to support Counter-Currents'
    #sepwc = 'words'
    soup3 = BeautifulSoup(requests.get(URL).content, 'html.parser')
    title = soup3.find('h1', class_="entry-title").text
    text = soup3.find('div', class_="entry-content").text
    title2 = soup3.title.text
    #t2 = text.split(sepcomments, 1)[0]
    #t3 = t2.split(sepwc, 1)
    #if (text.find('If you want to support Counter-Currents') != -1): 
    #    nocomments = text.split(sepcomments, 1)[0]
    #else: 
    #    nocomments = text
    text_data[title] = {}
    text_data[title]['title2'] = title2
    text_data[title]['url'] = url
    text_data[title]['content'] = text
    #text_data[title]['text_unedited'] = t2
    #text_data[title]['wc_text_listtuple'] = t3

a_text8 = pd.DataFrame(text_data8).T
#a_text8['wc_cc'], a_text8['editedtext'] = a_text8['wc_text_listtuple'].str[0], a_text8['wc_text_listtuple'].str[1]

#pulled at date save to txt & csv
a_text8.to_csv(r'CounterCurrentsData3500plus_pulled_' + today + '.txt')
a_text8.to_csv(r'CounterCurrentsData3500plus_pulled_' + today + '.csv')

concat = pd.concat([a_text,a_text2,a_text3,a_text4,a_text5,a_text6,a_text7,a_text8])

print(len(concat['url'].values))

pd.set_option('display.max_rows', None)
#val = concat
#display(val)
display(concat.head())

concat.to_pickle(r'CC_all_pickle' + today + '.pkl')