# -*- coding: utf-8 -*-


"""
aa*
The letter a is written, followed by a* (read as a star) which means “any number
of a’s, including 0 of them.” In this way, we can guarantee that the letter a is written
at least once.

(cc)*
Any even number of things can be grouped into pairs, so in order to enforce this
rule about even things, you can write two c’s, surround them in parentheses, and
write an asterisk after it, meaning that you can have any number of pairs of c’s
(note that this can mean 0 pairs, as well).

(d | )
Adding a bar in the middle of two expressions means that it can be “this thing or
that thing.” In this case, we are saying “add a d followed by a space or just add a
space without a d.” In this way we can guarantee that there is, at most, one d, followed
by a space, completing the string.

test regular expression
http://www.regexpal.com/
"""
"""
In fact, most functions
that take in a string argument (e.g., find(id="aTagIdHere")) will also take in a regular
expression just as well.
"""

import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)
images = bsObj.findAll("img",{"src":re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
for image in images:
    print(image["src"])

"""
A regular expression can be inserted as any argument in a BeautifulSoup expression,
allowing you a great deal of flexibility in finding target elements.
"""

