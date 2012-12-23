#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Isis Agora Lovecruft'
SITENAME = u'Patterns in the Void'
SITEURL = 'https://patternsinthevoid.net/blog/'

# Dev settings:
DELETE_OUTPUT_DIRECTORY = True

# Timezones, language, and metadata:
TIMEZONE = 'UTC'
DEFAULT_LANG = u'en'
DEFAULT_DATE = 'fs' # use filesystem metadata to get the creation date
DEFAULT_DATE_FORMAT = '%A %d %B %Y'
DEFAULT_CATEGORY = '/dev/random' # if no "Category: " in post, use this
USE_FOLDER_AS_CATEGORY = True


# Blogroll
LINKS =  (('Contact', 'https://patternsinthevoid.net/isis'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/#!/isislovecruft'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 3