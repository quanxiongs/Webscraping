# -*- coding: utf-8 -*-
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read())
print(bsObj.h1)

## handle error
try:
    html = urlopen("http://www.pythonscraping.com/pages/page1.html")
except urllib.error.HTTPError as e:
    print(e)
#return null, break, or do some other "Plan B"
else:
    pass
#program continues. Note: If you return or break in the
#exception catch, you do not need to use the "else" statement


#if beautifulsoup is attempting to access a tag on a None object itself will
#result in an AttributeError
print(bsObj.nonExistentTag.someTag)

badcontent = bsObj.nonExistentTag
if badcontent ==None:
    print("Tag was not found")

#즉 urlopen이나 beautifulsoup에서 에러가 나면 None을 반환한다
#so correct code will be like this
def gettitle(url):
    try:
        html = urlopen(url)
    except urllib.error.HTTPError as e:
        return(None)
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1
    except AttributeError as e:
        return(None)
    return title

title = gettitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
    print("title could not be found")
else:
    print(title)
        
#this kind of code is not so ideal , because of the complexity
#In addition to the aesthetics of the line, even the slightest 
#change to the website by a site administrator might break your web scraper altogether.
#So what are your options?
bsObj.findAll("table")[4].findAll("tr")[2].find("td").findAll("div")[1].find("a")
#we should think of alternatives

def getgreen(url):
    try:
        html = urlopen(url)
    except urllib.error.HTTPError as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html,"lxml")
    except AttributeError as e:
        print(e)
        return None
    namelist = bsObj.findAll("span",{"class":"green"})
    for name in namelist:
        print(name.get_text())

getgreen("http://www.pythonscraping.com/pages/warandpeace.html")
#Now, we’re calling bsObj.findAll(tagName, tagAttributes) in order to 
#get a list of all of the tags on the page, rather than just the first.

#.get_text() strips all tags from the document you are working
#with and returns a string containing the text only.
#.get_text() should always be the last thing you do


