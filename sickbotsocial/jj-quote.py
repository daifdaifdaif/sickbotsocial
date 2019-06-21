import markovify
import json
import sys
import re

from config import *
from print_quote import *
from clean_tweet import clean_tweet


import random
from random import randint

import tweepy


# LOAD CORPUS TEXT FILE
with open (corpus_file) as f:
	corpus_text = f.read()


#TWITTER LOGIN
if run_offline == 0:
	print("logging in")	
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)    
	auth.set_access_token(access_token, access_secret)
	api = tweepy.API(auth)

	print("logged in")


# SET AMOUNT OF TWEETS TO GENERATE
if run_offline == 0:
	j = randint(1,max_tweet_amount)
else:
	j = 5


# open files to write to
f = open(corpus_file,"a")
f2 = open(archive_file,"a")

# GENERATE TWEETS
i = 0
while i < j:
		
	# create text model
	k = randint(markov_state_size_range[0],markov_state_size_range[1])	
	text_model = markovify.NewlineText(corpus_text, state_size=k)
	

	# generate until we've got a new tweet
	tweet = None
	while tweet == None:
		length = randint(min_length,max_length)
		overlap = random.uniform(min_overlap,max_overlap)
		tweet = text_model.make_short_sentence(length,max_overlap_ratio=overlap)
	
	
	if run_offline == 0:
		# online -> post tweet
		
		f2.write(tweet + "\n")
		api.update_status(tweet)
		print("Tweeted: " + tweet + " (Generated with Length: " + str(length) + " | State Size: " + str(k) + " | Overlap: " + str(overlap) + ")")
		
		#ADD TO CORPUS

		f.write(tweet + "\n")
		
	else:
		# we're offline -> only output the tweet
		print(tweet)
		main_print_function(tweet, story=False, post=False)
	i += 1
	
f.close();
f2.close();


# INTERACT WITH JJ TWEETS
if run_offline == 0:
	
	# check last checked id
	f = open(id_file,"r+")
	last_id = f.readline()
	f.close()

	print("reading tweets")
	tweets = api.user_timeline(user_id=jj_user_id, count=20, tweet_mode='extended', since_id=last_id)
	print("found " + str(len(tweets)) + " new tweets by @sickbutsocial")


	for tweet in tweets:

		# interact with jj tweets
	
		if react_to_jj == 1:
			
			# check for trigger words
			
			if tweet.in_reply_to_screen_name == None:
				reply_check = "empty"
			else:
				reply_check = tweet.in_reply_to_screen_name
			
			if any(ext in tweet.full_text for ext in trigger_words) or any(ext in reply_check for ext in trigger_words):
	

				# generate an answer
				answer = None
				while answer == None:
				
					length = randint(min_words,max_words)
					overlap = random.uniform(min_overlap,max_overlap)
					
					
					# weighted random: whether to start answer with defined words
					rand_sel = randint(0,5)
					if rand_sel == 0:
					
						answer = text_model.make_sentence_with_start("du", strict=False, max_words=length, max_overlap_ratio=overlap)
						
					elif rand_sel == 1:
					
						answer = text_model.make_sentence_with_start("ich", strict=False, max_words=length, max_overlap_ratio=overlap)		
						
					else:
						answer = text_model.make_short_sentence(length,max_overlap_ratio=overlap)				
					
				
				answer = "@sickbutsocial " + answer
				if run_offline == 0:
					# post answer, fav original tweet
					api.update_status(answer,tweet.id)
					api.create_favorite(tweet.id)
	

		# clean up text and add to archive
		text = clean_tweet(tweet.full_text)
	
		if run_offline == 0:
			f = open(corpus_file,"a")
			f.write(text.encode('utf-8') + "\n")
			f.close()


	# save id of last checked tweet
	if len(tweets) > 0:
		f = open(id_file,"w")
		f.write(str(tweets[0].id))
		f.close()
		
	
	
	## CHECK MY OWN TWEETS
	
	print("reading tweets by me")
	tweets = api.user_timeline(user_id=bot_id, count=3, tweet_mode='extended')
	print("found " + str(len(tweets)) + " new tweets by @sickbotsocial")


	for tweet in tweets:

		# ANSWER TO MY TWEETS ABOUT ME <3 
	
		if react_to_myself == 1:
			
			# check for trigger words
			
			
			if any(ext in tweet.full_text for ext in trigger_words):
	

				# generate answer
				answer = None
				while answer == None:
				
					length = randint(min_words,max_words)
					overlap = random.uniform(min_overlap,max_overlap)
					
					# weighted random to start answer with defined words
					rand_sel = randint(0,9)
					if rand_sel == 0:
					
						answer = text_model.make_sentence_with_start("bot", strict=False, max_words=length, max_overlap_ratio=overlap)
						
					elif rand_sel == 1:
					
						answer = text_model.make_sentence_with_start("ich", strict=False, max_words=length, max_overlap_ratio=overlap)		
						
					else:
						answer = text_model.make_short_sentence(length,max_overlap_ratio=overlap)				
					
				answer = "@sickbotsocial " + answer
				if run_offline == 0:
					new_tweet = api.update_status(answer,tweet.id)
					# api.create_favorite(tweet.id)
					# api.retweet(new_tweet.id)
	
