#!/bin/python
# -*- coding: utf-8 -*-

import tweepy
import os

import urllib2

from config import *
from clean_tweet import clean_tweet
from print_quote import *


# GLOBALS
posts_to_scan = 50


# FUNCTION: GET USER IDs OF PEOPLE WHO FAVED A TWEET
# workaround using urllib2
def get_user_ids_of_post_likes(post_id):
    try:
        json_data = urllib2.urlopen('https://twitter.com/i/activity/favorited_popup?id=' + str(post_id)).read()
        found_ids = re.findall(r'data-user-id=\\"+\d+', json_data)
        unique_ids = list(set([re.findall(r'\d+', match)[0] for match in found_ids]))
        return unique_ids
    except urllib2.HTTPError:
        return False




# READING PRINTED TWEETS
f = open(printed_tweets_file, "rw+")
printed_tweets = f.readlines()

f2 = open(corpus_file,"a")



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
	print("problem reading tweets. enter credentials in config.py and check your twitter API key.")

for tweet in tweets:

# rt alleine zählt nicht wegen hurensohn bot
	if tweet.favorite_count > 0 :
		print("found ID: " + str(tweet.id) + " | Favs: " + str(tweet.favorite_count))
		
		if tweet.retweet_count >= retweet_threshold:
			post_img = True
		elif tweet.favorite_count >= like_threshold:
			post_img = True
		else:
			post_img = False
		

		text = tweet.full_text.encode("utf-8")
	
	
		if (text + "\n") in printed_tweets:
			print ("already printed this tweet")
	
		else:				
			
			# send tweet to print_image.py
			
			# remove whitespace if there's one at the start 
			if text[0] == " ":
				text = text[1:]
				
				
			main_printer(text, post=post_img)
			
			# write to printed tweets
			f.write(text+"\n")
			
			print("printed tweet")
			
			# add faveds tweet to corpus file, enables weightening by user likes
			
			text = clean_tweet(tweet.full_text)
			f2.write(text.encode('utf-8') + "\n")
			
			# check for weighted accounts and write again to file if true
			
			faves_by = get_user_ids_of_post_likes(tweet.id)
			if faves_by != False:
				if any(ext in faves_by for ext in weighted_user_ids):
					print("found fav by weightened user")
					f2.write(text.encode('utf-8') + "\n")

			
			amt_posted += 1	
				
			if amt_posted == max_posts_to_do_at_once:
				break

			

f.close()
f2.close()
