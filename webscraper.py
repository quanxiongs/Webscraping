# -*- coding: utf-8 -*-

import os
os.getcwd()
from bs4 import BeautifulSoup
import requests
import pandas as pd
from pandas import Series, DataFrame

url = 'http://www.ucop.edu/operating-budget/\
budgets-and-reports/legislative-reports/2013-14-legislative-session.html'

result = requests.get(url)
c = result.content
soup = BeautifulSoup(c, "lxml")

#here we find particular part from the soup object
summary = soup.find('div',{'class':'list-land','id':'content'})
tables = summary.find_all('table')
#here we find all the contents of the table

print(tables)

data=[]
rows = tables[0].findAll('tr')

for tr in rows:
    cols = tr.findAll('td')
    for td in cols:
        text = td.find(text=True)
        print(text)
        data.append(text)
        
reports=[]
date=[]
index = 0

for item in data:
    if 'pdf' in item:
        date.append(data[index-1])
        reports.append(item.replace(u'\xa0',u' '))
    index +=1

date = Series(date)
reports = Series(reports)
legislative_df = pd.concat([date,reports],axis=1)
legislative_df.columns=['Date','Report'] 

legislative_df