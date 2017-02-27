# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
from pandas import read_html

url = 'http://www.fdic.gov/bank/individual/failed/banklist.html'

#first you should install html5lib and beautifulsoup4
dframe_list = pd.io.html.read_html(url)

dframe=dframe_list[0]

dframe.columns.values

dframe

