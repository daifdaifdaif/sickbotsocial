import markovify
import json
import sys
import re

from config import *
from print_quote import *


import random
from random import randint

import tweepy



# CHECK WHETHER WE'RE LIVE

total = len(sys.argv)
print(total)
if total > 1:
	if sys.argv[1] == "test":
		test = 1
		print("test mode engaged")



#LOAD CORPUS TEXT FILE
print("reading corpus: "+corpus_file)
with open (corpus_file) as f:
	text = f.read()


#TWITTER LOGIN
if test == 0:
	print("logging in")	
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)    
	auth.set_access_token(access_token, access_secret)
	api = tweepy.API(auth)

	print("logged in")




# SET AMOUNT OF TWEETS TO GENERATE
if test == 0:
	j = randint(1,max_tweet_amount)
else:
	j = 1



i = 0

# GENERATE TWEETS
while i < j:
		
	k = randint(markov_state_size_range[0],markov_state_size_range[1])	
	text_model = markovify.NewlineText(text, state_size=k)
	

	# TRY TO GENERATE
	tweet = None
	while tweet == None:
		length = randint(min_length,max_length)
		overlap = random.uniform(min_overlap,max_overlap)
		tweet = text_model.make_short_sentence(length,max_overlap_ratio=overlap)
	

	if test == 0:
		# POST TWEET

		api.update_status(tweet)
		print("Tweeted: " + tweet + " (Generated with Length: " + str(length) + " | State Size: " + str(k) + " | Overlap: " + str(overlap) + ")")
		#ADD TO CORPUS
		f = open(corpus_file,"a")
		f.write(tweet + "\n")
		
	else:
		
		print(tweet + " (Generated with Length: " + str(length) + " | State Size: " + str(k) + " | Overlap: " + str(overlap) + ")")
		main_printer(tweet, story=False, post=False)
	i += 1
	
f.close();

# ADD RECENT JJ TWEETS TO CORPUS
if test == 0:
	f = open(id_file,"r+")
	last_id = f.readline()
	f.close()

	print("reading tweets")
	tweets = api.user_timeline(user_id=jj_user_id, count=20, tweet_mode='extended', since_id=last_id)
	print("found " + str(len(tweets)) + " new tweets by @sickbutsocial")


	for tweet in tweets:

		# RETWEET JJs TWEETS ABOUT ME <3 
	
		if retweet_jj == 1:
			
			# CHECK FOR TRIGGER WORDS
			
			# python "any ext in ..." function will not work with null, set string to check accordingly
			if tweet.in_reply_to_screen_name == None:
				reply_check = "empty"
			else:
				reply_check = tweet.in_reply_to_screen_name
			
			if any(ext in tweet.full_text for ext in trigger_words) or any(ext in reply_check for ext in trigger_words):
	

				# TRY TO GENERATE
				answer = None
				while answer == None:
				
					length = randint(min_words,max_words)
					overlap = random.uniform(min_overlap,max_overlap)
					
					rand_sel = randint(0,3)
					
					if rand_sel == 0:
					
						answer = text_model.make_sentence_with_start("du", strict=False, max_words=length, max_overlap_ratio=overlap)
						
					elif rand_sel == 1:
					
						answer = text_model.make_sentence_with_start("ich", strict=False, max_words=length, max_overlap_ratio=overlap)		
						
					else:
						answer = text_model.make_short_sentence(length,max_overlap_ratio=overlap)				
					
				answer = "@sickbutsocial " + answer
				if test == 0:
					api.update_status(answer,tweet.id)
					api.create_favorite(tweet.id)
	

		# CLEAN UP
	
		text = re.sub(r'@\S*', "", tweet.full_text)
		text = re.sub(r'http\S*', "", text)
		text = re.sub(r'  ', " ", text)
		text = re.sub(r'RT', "", text)
	
		
		if test == 0:
			f = open(corpus_file,"a")
			f.write(text.encode('utf-8') + "\n")
			f.close()


	#  WRITE LAST CHECKED TWEET ID TO FILE
	if len(tweets) > 0:
		#if test == 0:
		f = open(id_file,"w")
		f.write(str(tweets[0].id))
		f.close()
	
	
	
	
	## CHECK MY OWN TWEETS
	
	print("reading tweets by me")
	tweets = api.user_timeline(user_id=bot_id, count=3, tweet_mode='extended')
	print("found " + str(len(tweets)) + " new tweets by @sickbotsocial")


	for tweet in tweets:

		# ANSWER TO MY TWEETS ABOUT ME <3 
	
		if retweet_myself == 1:
			
			# CHECK FOR TRIGGER WORDS
			
			# python "any ext in ..." function will not work with null, set string to check accordingly

			
			if any(ext in tweet.full_text for ext in trigger_words):
	

				# TRY TO GENERATE
				answer = None
				while answer == None:
				
					length = randint(min_words,max_words)
					overlap = random.uniform(min_overlap,max_overlap)
					
					rand_sel = randint(0,10)
					
					if rand_sel == 0:
					
						answer = text_model.make_sentence_with_start("bot", strict=False, max_words=length, max_overlap_ratio=overlap)
						
					elif rand_sel == 1:
					
						answer = text_model.make_sentence_with_start("ich", strict=False, max_words=length, max_overlap_ratio=overlap)		
						
					else:
						answer = text_model.make_short_sentence(length,max_overlap_ratio=overlap)				
					
				answer = "@sickbotsocial " + answer
				if test == 0:
					new_tweet = api.update_status(answer,tweet.id)
					# api.create_favorite(tweet.id)
					# api.retweet(new_tweet.id)
	
