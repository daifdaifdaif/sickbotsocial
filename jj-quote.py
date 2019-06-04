import markovify
import json
import sys
import re

from config import *

import random
from random import randint

import tweepy

# GLOBALS
test=0
corpus_file = "/home/pi/jj-bot/jj-nomention-bot.txt"
chain_file = "/home/pi/jj-bot/jj.json"
id_file = "/home/pi/jj-bot/id.txt"
retweet_jj = 1

# VARIABLES FOR QUOTES
min_length=30
max_length=230
min_words=5
max_words=20
min_overlap=0.35
max_overlap=0.85



# CREDENTIALS


# CHECK WHETHER WE'RE LIVE

total = len(sys.argv)
print(total)
if total > 1:
	if sys.argv[1] == "test":
		test = 1
		print("test mode engaged")



#GENERATE MODEL
print("reading corpus: "+corpus_file)
with open (corpus_file) as f:
	text = f.read()


#TWITTER LOGIN

print("logging in")	
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)    
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

print("logged in")



i = 0

#AMOUNT OF TWEETS TO GENERATE
j = randint(1,3)



# GENERATE TWEETS
while i < j:
		
	k = randint(1,3)	
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
	i += 1
	
f.close();
print("Finished")


# ADD RECENT JJ TWEETS TO CORPUS

f = open(id_file,"r+")
last_id = f.readline()
f.close()
print("last id: " + last_id)

print("reading tweets")
tweets = api.user_timeline(user_id="878210144827580416", count=20, tweet_mode='extended', since_id=last_id)
print("found " + str(len(tweets)) + " new tweets by @sickbutsocial")


for tweet in tweets:

	# CLEAN UP
	
	text = re.sub(r'@\S*', "", tweet.full_text)
	text = re.sub(r'http\S*', "", text)
	text = re.sub(r'  ', " ", text)
	text = re.sub(r'RT', "", text)
	
	# RETWEET JJs TWEETS ABOUT ME <3 
	
	
	if retweet_jj == 1:
		if "bot" in text:
	

			# TRY TO GENERATE
			answer = None
			while answer == None:
				while " ich " not in str(answer):
					length = randint(min_words,max_words)
					overlap = random.uniform(min_overlap,max_overlap)
					answer = text_model.make_sentence_with_start("du", strict=False, max_words=length, max_overlap_ratio=overlap)
			answer = "@sickbutsocial " + answer
			if test == 0:
				api.update_status(answer,tweet.id)
				api.create_favorite(tweet.id)
	
	
	
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
	
