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

