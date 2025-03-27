from collections import namedtuple

import os
import yaml

AUTHOR = "Robert Bossaert"
SITENAME = "Robert Bossaert"
SITEURL = '{}'.format(os.getenv('SITEURL', 'http://localhost:{}'.format(os.getenv('PORT', '8000'))))

PATH = "content"

TIMEZONE = "Europe/Amsterdam"

DEFAULT_LANG = "en"

# Theme settings
THEME= "themes/default"
CSS_FILE = 'styles.css'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = (('About', '/about.html'),
            ('About', '/about.html'),
            ('Tags', '/tags.html'),)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

STATIC_PATHS = [
    'images',
]

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

with open('data/books.yml') as books:
    books_converted = yaml.safe_load(books.read())
    BOOKS = []
    for book in books_converted:
        BOOKS.append(
            namedtuple('Books', book.keys())(**book)
        )

with open('data/sites.yml') as sites:
    sites_converted = yaml.safe_load(sites.read())
    SITES = []
    for site in sites_converted:
        SITES.append(
            namedtuple('Sites', site.keys())(**site)
        )