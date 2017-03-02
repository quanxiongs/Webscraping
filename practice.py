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

""" this is find method's arguments
findAll(tag, attributes, recursive, text, limit, keywords)
find(tag, attributes, recursive, text, keywords)

The recursive argument is a boolean. How deeply into the document do you want to
go? If recursion is set to True, the findAll function looks into children, and children’s
children, for tags that match your parameters. If it is false, it will look only at
the top-level tags in your document. By default, findAll works recursively (recur
sive is set to True); it’s generally a good idea to leave this as is, unless you really know
what you need to do and performance is an issue.

The text argument is unusual in that it matches based on the text content of the tags,
rather than properties of the tags themselves. For instance, if we want to find the
number of times “the prince” was surrounded by tags on the example page, we could
replace our .findAll() function in the previous example with the following lines:
nameList = bsObj.findAll(text="the prince")
print(len(nameList))
The output of this is “7.”

The limit argument, of course, is only used in the findAll method; find is equivalent
to the same findAll call, with a limit of 1. You might set this if you’re only interested
in retrieving the first x items from the page. Be aware, however, that this gives
you the first items on the page in the order that they occur, not necessarily the first
ones that you want.
The keyword argument allows you to select tags that contain a particular attribute.
For example:
allText = bsObj.findAll(id="text")
print(allText[0].get_text())
"""
