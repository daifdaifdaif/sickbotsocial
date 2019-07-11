#!/bin/python
# -*- coding: utf-8 -*-

import re
from HTMLParser import HTMLParser

# FUNCTION: CLEAN UP TWEET TEXT
# removes mentions, links, etc
# converts url escaped characters


def clean_tweet(s):
	h = HTMLParser()

	s = re.sub(r'[&].+\s', '', s)
	s = re.sub(r'@\S*', "", s)
	s = re.sub(r'http\S*', "", s)
	s = re.sub(r'  ', " ", s)
	s = re.sub(r'RT', "", s)
	try:
		s2 = h.unescape(s)
		return s2
	except:
		return s
