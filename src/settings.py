import os

AUTHOR = 'Derek Payton'
SITENAME = 'dmpayton.com'

SITEURL = 'http://dmpayton.com'
FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/category.%s.rss.xml'
TAG_FEED_RSS = 'feeds/tag.%s.rss.xml'

LOCALE = 'en_US.UTF-8'
TIMEZONE = 'US/Pacific'

DEFAULT_PAGINATION = False
PDF_GENERATOR = False
RELATIVE_URL = False
REVERSE_CATEGORY_ORDER = True

PATH = 'content'
THEME = 'theme'
OUTPUT_PATH = '../'
STATIC_PATHS = ('files', 'images')

GITHUB_URL = 'http://github.com/dmpayton/'
GOOGLE_ANALYTICS = 'UA-2045660-5'
