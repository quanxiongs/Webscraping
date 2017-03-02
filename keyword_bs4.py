# -*- coding: utf-8 -*-
"""
Keep in mind that anything that can be done with keyword can also
be accomplished using techniques we will discuss later in this chapter
(see Regular Expressions and Lambda Expressions).

For instance, the following two lines are identical:
bsObj.findAll(id="text")
bsObj.findAll("", {"id":"text"})

In addition, you might occasionally run into problems using key
word

if you try
the following call, you’ll get a syntax error due to the nonstandard
use of class:
bsObj.findAll(class="green")
Instead, you can use BeautifulSoup’s somewhat clumsy solution,
which involves adding an underscore:
bsObj.findAll(class_="green")
Alternatively, you can enclose class in quotes:
bsObj.findAll("", {"class":"green"}
"""

