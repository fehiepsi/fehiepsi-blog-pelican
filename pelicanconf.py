#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'fehiepsi'
SITENAME = u"fehiepsi's blog"
SITEURL = ''

TIMEZONE = 'Asia/Ho_Chi_Minh'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('bình yên', 'http://binhyen.livejournal.com/'),
          ('What\'s new', 'http://terrytao.wordpress.com/'),
          ('Zen Habits', 'http://zenhabits.net/'),
          ('A Quiet Place', 'http://genhara-chan.tumblr.com/'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DEFAULT_DATE_FORMAT = '%b %d, %Y'

# Set the article URL
ARTICLE_URL = 'blog/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'

# Title menu options
MENUITEMS = (('Archives', '/archives.html'),)

# Theme and plugins
#  Theme requires http://github.com/duilio/pelican-octopress-theme/
#  Plugins require http://github.com/getpelican/pelican-plugins/
THEME = '../pelican-octopress-theme/'
PLUGIN_PATH = '../pelican-plugins/'
PLUGINS = ['summary',]
#PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
#           'liquid_tags.include_code', 'liquid_tags.notebook',
#           'liquid_tags.literal']


