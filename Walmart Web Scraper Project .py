#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import libraries 
 
from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime


# In[14]:


# connect to website 
URL = 'https://www.walmart.com/ip/Solar-Eclipse-Glasses-10-pack-2024-CE-and-ISO-Certified-Multicolor-Safe-Shades-for-Direct-Sun-Viewing-MedicalKingUsa/5296006568?from=/search'

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

page = requests.get(URL,headers=headers)

soup1 = BeautifulSoup(page.content, 'html.parser')

soup2 = BeautifulSoup(soup1.prettify(), 'html.parser') #makes it look better

title = soup2.find(id='main-title').get_text()

price = soup2.find(itemprop='price').get_text()

print(title)
print()
print(price)


# In[15]:


price = price.strip()[1:]
title = title.strip()

print(title)
print(price)


# In[19]:


# adding date stamp or time stmap 

import datetime

today = datetime.date.today()
print(today)


# In[20]:


import csv

header = ['Title','Price', 'Date']
data = [title,price,today]

type(data)

#with open('WalmartWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
    #writer = csv.writer(f)
    #writer.writerow(header) #initial insertion of header
    #writer.writerow(data) #initial insertion of data


# In[25]:


# checking if date inserted
import pandas as pd

df = pd.read_csv(r'/Users/khadijahiscandri/WalmartWebScraperDataset.csv')

print(df)


# In[ ]:


# append data to spreadsheet

with open('WalmartWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data) 


# In[31]:


# going to automate the appending process
# putting it in on a timer, once a day 

def check_price():
    URL = 'https://www.walmart.com/ip/Solar-Eclipse-Glasses-10-pack-2024-CE-and-ISO-Certified-Multicolor-Safe-Shades-for-Direct-Sun-Viewing-MedicalKingUsa/5296006568?from=/search'

    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

    page = requests.get(URL,headers=headers)

    soup1 = BeautifulSoup(page.content, 'html.parser')

    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser') #makes it look better

    title = soup2.find(id='main-title').get_text()

    price = soup2.find(itemprop='price').get_text()
    
    price = price.strip()[1:]
    title = title.strip()
    
    import datetime

    today = datetime.date.today()
    
    import csv
    
    header = ['Title','Price', 'Date']
    data = [title,price,today]
    
    with open('WalmartWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data) 
        
    if(price > 12):
        you_got_mail()
    


# In[27]:


while(True):
    check_price()
    time.sleep(86400)


# In[28]:


import pandas as pd

df = pd.read_csv(r'/Users/khadijahiscandri/WalmartWebScraperDataset.csv')

print(df)


# In[33]:


def you_got_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('kii7594@mavs.uta.edu', 'Uta154069!2022')
    
    subject = 'The Eclipse Glasses you want is below $12! Get it now!'
    body = 'Khadijah, your wish list product is available!'
    
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'kii7594@mavs.uta.edu',
        msg
    
    )
    
    


# In[ ]:




