# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html)
for link in bsObj.findAll("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])

#이렇게 코트를 짜면 쓸대없는 링크까지 너무 많이 포함 됨
#이렇게 바꿔보자

"""
They reside within the div with the id set to bodyContent
The URLs do not contain semicolons
The URLs begin with /wiki/
"""


import re
html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html)
for link in bsObj.find("div",{"id":"bodyContent"}).findAll("a",
                       href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])
        
"""
Of course, having a script that finds all article links in one, hardcoded Wikipedia article,
while interesting, is fairly useless in practice. We need to be able to take this code and
transform it into something more like the following:

A single function, getLinks, that takes in a Wikipedia article URL of the form
/wiki/<Article_Name> and returns a list of all linked article URLs in the same form.

A main function that calls getLinks with some starting article, chooses a random
article link from the returned list, and calls getLinks again, until we stop the program
or until there are no article links found on the new page.
"""

import datetime
import random

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html)
    return(bsObj.find("div",{"id":"bodyContent"}
                ).findAll("a",
                href=re.compile("^(/wiki/)((?!:).)*$")))
links = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0:
    newArticle = links[random.randint(0,len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)
    
"""
While computers are great at calculating correct answers, they’re terrible at just making things up. For this reason,
random numbers can be a challenge. Most random number algorithms strive to produce an evenly distributed and
hard-to-predict sequence of numbers, but a “seed” number is needed to give these algorithms something to work
with initially. The exact same seed will produce the exact same sequence of “random” numbers every time, so for
this reason I’ve used the system clock as a starter for producing new sequences of random numbers, and, thus, new
sequences of random articles. This makes the program a little more exciting to run.
"""

"""
the deep Web is relatively easy to scrape. In fact, there are many tools in this book that will
teach you how to crawl and scrape information from many places that Google bots can’t go
"""

"""
The general approach to an exhaustive site crawl is to start with a top-level page (such as
the home page), and search for a list of all internal links on that page. Every one of those
links is then crawled, and additional lists of links are found on each one of them,
triggering another round of crawling.
"""

#그런데 여기서 link 중복의 문제가 발생한다.
"""
In order to avoid crawling the same page twice, it is extremely important that all internal
links discovered are formatted consistently
"""

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html)
    for link in bsObj.findAll("a", href = re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks("")


#something about recursion
"""
Python has a default recursion limit (how many times programs can recursively call themselves) of 1,000.
Because Wikipedia’s network of links is extremely large, this program will eventually hit that recursion
limit and stop, unless you put in a recursion counter or something to prevent that from happening.
"""

