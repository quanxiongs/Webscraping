# -*- coding: utf-8 -*-

"""
very often in web scraping you’re not looking for the content of a tag; you’re
looking for its attributes. This becomes especially useful for tags such as <a>, where
the URL it is pointing to is contained within the href attribute, or the <img> tag,
where the target image is contained within the src attribute.
"""

"""
Essentially, a lambda expression is a function that is passed into another function as a
variable; that is, instead of defining a function as f(x, y), you may define a function as
f(g(x), y), or even f(g(x), h(x)).

BeautifulSoup allows us to pass certain types of functions as parameters into the fin
dAll function. The only restriction is that these functions must take a tag object as an
argument and return a boolean. Every tag object that BeautifulSoup encounters is
evaluated in this function, and tags that evaluate to “true” are returned while the rest
are discarded.

For example, the following retrieves all tags that have exactly two attributes:
soup.findAll(lambda tag: len(tag.attrs) == 2)
That is, it will find tags such as the following:
<div class="body" id="content"></div>
<span style="color:red" class="title"></span>
"""
