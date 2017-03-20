# -*- coding: utf-8 -*-

import urllib.request

import urllib.parse

import re

from bs4 import BeautifulSoup

import os
os.getcwd()

defaultUrl = "http://cafe.naver.com/nexonjojo/"

f = urllib.request.urlopen(defaultUrl+"293917")

bsObj = BeautifulSoup(f,"lxml")
bsObj.findAll("iframe",{"name":"cafe_main"}).find("div")
bsObj.findAll("input",{"name" :"menuid"})[0]['value']
bsObj.findAll("html",{"lang":"ko"})[0].find("div",{"id":"content-area"})

#####################

articleURL = "http://cafe.naver.com/ArticleRead.nhn?articleid=294345&clubid=28334250"
html = urllib.request.urlopen(articleURL)
bsObj = BeautifulSoup(html,"lxml",from_encoding='CP949')
#bsObj = BeautifulSoup(html,"html.parser",from_encoding='utf-8')
#test = bsObj.findAll("div",{"class":"tbody m-tcol-c"})
test = bsObj.findAll()
strings = str(test)
with open("C:\\SparkCourse\\newscraping\\link\\test3.txt", 'wt', encoding='utf8') as testfile:
    testfile.write(strings)

#####################

test = bsObj.findAll("div",{"class":"fr"})[1].findAll("tr")[0].find("td",{"class":"m-tcol-c date"}).text
test = bsObj.findAll("div",{"class":"tbody m-tcol-c"})


####################



mainURL = "http://cafe.naver.com/nexonjojo.cafe?iframe_url=/nexonjojo/ArticleList.nhn%3Fsearch.clubid=28334250%26amp;search.boardtype=L"
html3 = urllib.request.urlopen(mainURL)
bsObj = BeautifulSoup(html3,"lxml")
linklist = bsObj.findAll("a", href = re.compile("^(/ArticleRead.nhn?)"))
linklist = bsObj.findAll("a")

bsObj.findAll("a",href = re.compile("^(/ArticleRead.nhn?)"))


<a href="/ArticleList.nhn?search.clubid=28334250&amp;search.menuid=1&amp;search.boardtype=L" target="cafe_main" onclick="goMenu('1');clickcr(this, 'mnu.normal','','',event);" class="gm-tcol-c b" id="menuLink1">자유 게시판</a>
http://cafe.naver.com/nexonjojo.cafe?iframe_url=/nexonjojo/294141/ArticleList.nhn%3Fsearch.clubid=28334250%26amp;search.menuid=1%26amp;search.boardtype=L

boardURL ="http://cafe.naver.com/nexonjojo.cafe?iframe_url=/nexonjojo/294141/ArticleList.nhn%3Fsearch.clubid=28334250%26amp;search.menuid=1%26amp;search.boardtype=L"
html2 = urllib.request.urlopen(boardURL)
bsObj = BeautifulSoup(html2,"lxml")
bsObj.findAll("a",href=re.compile("^(/ArticleRead.nhn?)"))

#######
import urllib.request

import urllib.parse

import re

from bs4 import BeautifulSoup


def getArticle(url):
    try:
        html = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html,'lxml',from_encoding="CP949")
    except AttributeError as e:
        print (e)
        return None
    try:
        temp = bsObj.findAll("div",{"class":"tbody m-tcol-c"})[0].text
    except IndexError as e:
        print (e)
        return None
    try:
        temp2 = bsObj.findAll("div",{"class":"fr"})[1].findAll("tr")[0].find("td",{"class":"m-tcol-c date"}).text
    except IndexError as e:
        print (e)
    try:
        temp3 = bsObj.findAll("input",{"name" :"menuid"})[0]['value']
    except IndexError as e:
        print (e)
        return None
    return (temp,temp2,temp3)



articleList = [] #origianl memory
timeList = [] 
menuList = []
for i in range(178182,294668):
    articleURL = ("http://cafe.naver.com/ArticleRead.nhn?articleid=%d" % i )+"&clubid=28334250"
    if getArticle(articleURL) == None:
        continue
    else:
        article, times, menu = getArticle(articleURL)
    #11 bug
    
    articleList.append(article)
    timeList.append(times)
    menuList.append(menu)


for item in articleList:
    newArticleList.append(item.replace(u'\xa0',u''))
newArticleList =[]

def replace_trash(unicode_string):
     for i in range(0, len(unicode_string)):
         try:
             unicode_string[i].encode("CP949")
         except:
              #means it's non-ASCII
              unicode_string=unicode_string.replace(unicode_string[i]," ") #replacing it with a single space
     return unicode_string


newArticleList = ([replace_trash(item) for item in newArticleList])



with open("articledump_final.txt",'w') as file:
    file.writelines( "%s\n" % item for item in newArticleList )
with open("timedump_final.txt",'w') as file:
    file.writelines( "%s\n" % item for item in timeList )
with open("menudump_final.txt",'w') as file:
    file.writelines( "%s\n" % item for item in menuList )


newArticleList = [k.strip() for k in newArticleList]
with open("articledump_strip.txt",'w') as file:
    file.writelines( "%s\n" % item for item in newArticleList )


import pandas as pd

content = pd.Series(newArticleList, name="content")
datetime = pd.Series(timeList,name="date")
boardmenu = pd.Series(menuList,name="menu_no")


Articles = pd.concat([content,datetime, boardmenu], axis =1)

Articles.to_csv("jojo.csv")

#####################



###
articleURL
%reset

len(articleList)
len(newArticleList)
print(articleList[1:100])