#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jamie Luck'
SITENAME = "delucks' Content"
TAGLINE = 'Tagline Here'

'''Custom theme implemented in this repo'''
THEME = 'theme'
DISPLAY_PAGES_ON_MENU = False

PATH = 'content'
LOAD_CONTENT_CACHE=False

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Links to show on the top-left hand corner of the main page
LINKS = (
    ('CLI', 'https://cli.jamieluck.com'),
    ('Github', 'https://github.com/delucks'),
    ('R&eacute;sum&eacute;', '/theme/JamesLuckResume.pdf?v=20160510'),
    ('Recipes', 'http://spicyboysauce.party/'),
    ('LinkedIn', 'https://linkedin.com/in/jamieluck')
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
