#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Jamie Luck'
SITENAME = "delucks' Blog"
TAGLINE = "How can our Words be Real if our Brains aren't Real?"
#SITEURL = 'https://blog.jamieluck.com'

'''Custom theme implemented at https://github.com/delucks/pelican-solarizedhack'''
THEME = os.path.expanduser('~/dev/pelican-solarizedhack')
DISPLAY_PAGES_ON_MENU = False

PATH = 'content'
LOAD_CONTENT_CACHE=False

#TIMEZONE = 'US/Eastern'
TIMEZONE = 'Etc/UTC'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Homepage', 'https://jamieluck.com/'),
    ('Recipes', 'http://spicyboysauce.party/'),
    ('Github', 'https://github.com/delucks')
)

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

'''
Other Nice Themes:
    svbhack
    cebong
    clean-blog
    SoMA{,2}
'''
