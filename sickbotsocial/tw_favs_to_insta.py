#!/bin/python
# -*- coding: utf-8 -*-

import tweepy
import os

from config import *

from print_quote import *


# GLOBALS
posts_to_scan = 50
max_posts_to_do_at_once = 2


# READING PRINTED TWEETS
f = open(printed_tweets_file, "rw+")
printed_tweets = f.readlines()




#TWITTER LOGIN

print("logging in")	
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)    
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)


amt_posted = 0

# READING TWEETS
try:
	tweets = api.user_timeline(user_id=bot_id, count=posts_to_scan, tweet_mode='extended')
	print("log in worked")
	print("reading tweets")
except:
	print("problem reading tweets. enter credentials in config.py")

for tweet in tweets:

# rt alleine zählt nicht wegen hurensohn bot
	if tweet.favorite_count > 0 :
		
		if tweet.retweet_count >= retweet_threshold:
			post_img = True
		elif tweet.favorite_count >= like_threshold:
			post_img = True
		else:
			post_img = False
		
		try:	
			text = tweet.full_text.encode("utf-8")
			print ("found faved tweet: " + text)
		
		
			if (text + "\n") in printed_tweets:
				print ("already printed this tweet")
		
			else:
			
				print("printing: "+text)
				main_printer(text, post=post_img)
				f.write(text+"\n")
				amt_posted += 1
				
				if amt_posted == max_posts_to_do_at_once:
					break
		
		except:
			print("error?!?!")
			

f.close()
