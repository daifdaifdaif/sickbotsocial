#!/bin/python
# -*- coding: utf-8 -*-

import re

# FUNCTION: CLEAN UP TWEET TEXT
# removes mentions, links, etc

def clean_tweet(s):
	s = re.sub(r'[&].+\s', '', s)
	s = re.sub(r'@\S*', "", s)
	s = re.sub(r'http\S*', "", s)
	s = re.sub(r'  ', " ", s)
	s = re.sub(r'RT', "", s)
	return s
