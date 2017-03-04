# -*- coding: utf-8 -*-
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages =set()
def getlinks(pageUrl):
    try:
        html=urlopen("http://en.wikipedia.org"+pageUrl)
    except urllib.error.HTTPError as e:
        print(e)
    bsObj = BeautifulSoup(html)
    try:
        print( bsObj.h1.get_text())
        print( bsObj.find(id='mw-content-text').findAll('p')[0])
        print(bsObj.find(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print('This page is missing something')
    for link in bsObj.findAll('a',href = re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print("---------\n"+ newPage)
                pages.add(newPage)
                getlinks(newPage)
    
getlinks("")



#Crawling outbound links
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
import urllib

pages = set()
random.seed(datetime.datetime.now())

#find all links that begin with a "/"
def getinternallink(bsObj,includeUrl):
    internalLinks=[]
    for link in bsObj.findAll('a', href = re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks

#Retreive a list of all external link
def getexternallink(bsObj, excludeUrl):
    externalLinks=[]
    for link in bsObj.findAll("a", href = re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks
    
def splitAddress(address):
    addressPart = address.replace("http://","").split("/")
    return(addressPart)

def getRandomLink(startingpage):
    html = urlopen(startingpage)
    bsObj = BeautifulSoup(html)
    externallinks = getexternallink(bsObj,splitAddress(startingpage)[0])
    if len(externallinks) == 0:
        internallinks = getinternallink(bsObj,splitAddress(startingpage)[0])
        return getRandomLink(internallinks[random.randint(0,len(internallinks)-1)])
    else:
        return externallinks[random.randint(0,len(externallinks)-1)]

def followExternalOnly(startingpage):
    externalLink = getRandomLink(startingpage)
    print('Random External Link :' + externalLink)
    followExternalOnly(externalLink)

followExternalOnly("http://oreilly.com")

#but to avoid access dednied problem we use
class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

opener = AppURLopener()
#response = opener.open('http://httpbin.org/user-agent')

"""
and revise function like this
"""
def getRandomLink(startingpage):
    html = opener.open(startingpage)
    bsObj = BeautifulSoup(html)
    externallinks = getexternallink(bsObj,splitAddress(startingpage)[0])
    if len(externallinks) == 0:
        internallinks = getinternallink(bsObj,splitAddress(startingpage)[0])
        return getRandomLink(internallinks[random.randint(0,len(internallinks)-1)])
    else:
        return externallinks[random.randint(0,len(externallinks)-1)]
