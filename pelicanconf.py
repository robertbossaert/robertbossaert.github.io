from collections import namedtuple

import os
import yaml

AUTHOR = "Robert Bossaert"
SITENAME = "Robert Bossaert"
SITE_DESCRIPTION = "Passionate software engineer and code tinkerer."
SITEURL = '{}'.format(os.getenv('SITEURL', 'http://localhost:{}'.format(os.getenv('PORT', '8000'))))

PATH = "content"

# Date / time
DEFAULT_LANG = "en"
DEFAULT_DATE_FORMAT = "%B %d, %Y"
LOCALE = "en_US"
TIMEZONE = "Europe/Amsterdam"

# Theme settings
THEME= "themes/default"
CSS_FILE = 'styles.css'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = (('About', '/about'),
            ('Archives', '/archives'),
            ('Categories', '/categories'),
            ('Atom', '/categories'),)

# Article settings
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

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
