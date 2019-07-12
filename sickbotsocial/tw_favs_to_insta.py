#!/bin/python
# -*- coding: utf-8 -*-

import tweepy
import os

import urllib2

from config import *
from clean_tweet import clean_tweet
from print_quote import *


# GLOBALS
posts_to_scan = 75


# FUNCTION: GET USER IDs OF PEOPLE WHO FAVED A TWEET
# workaround using urllib2
def get_user_ids_of_post_likes(post_id):
    try:
        json_data = urllib2.urlopen(
            'https://twitter.com/i/activity/favorited_popup?id=' + str(post_id)).read()
        found_ids = re.findall(r'data-user-id=\\"+\d+', json_data)
        unique_ids = list(set([re.findall(r'\d+', match)[0]
                               for match in found_ids]))
        return unique_ids
    except urllib2.HTTPError:
        return False


# READING PRINTED TWEETS
f3 = open(printed_tweets_file, "rw+")
printed_tweets = f3.readlines()

f2 = open(corpus_file, "a")

f4 = open(archive_file, "a")

# TWITTER LOGIN

print("logging in")
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

amt_posted = 0

# READING TWEETS
try:
    tweets = api.user_timeline(
        user_id=bot_id, count=posts_to_scan, tweet_mode='extended')
    print("log in worked")
    print("reading tweets")
except:
    print("problem reading tweets. enter credentials in config.py and check your twitter API key.")

for tweet in tweets:

    # check for fav and retweet threshold
    if tweet.favorite_count >= story_fav_threshold or \
			tweet.retweet_count >= story_post_retweet_threshold:

		# check for fav and retweet threshold to post
        if tweet.retweet_count >= post_retweet_threshold:
            post_img = True
        elif tweet.favorite_count >= post_fav_threshold:
            post_img = True
        elif tweet.retweet_count + tweet.favorite_count >= post_combined_threshold:
            post_img = True
        else:
            post_img = False

        text = tweet.full_text.encode("utf-8")

        if (text + "\n") in printed_tweets:
            print ("already printed this tweet")

        else:

            # remove whitespace if there's one at the start
            if text[0] == " ":
                text = text[1:]

            # send tweet to print_image.py
            main_print_function(text, post=post_img)

            # write to printed tweets
            f3.write(text+"\n")

            print("printed tweet")

            # add faveds tweet to corpus file, enables weightening by user likes

            text = clean_tweet(tweet.full_text)

            try:
                f2.write(text + "\n")
            except:
                print("f2 write error")

            try:
                f4.write(text + "\n")
            except:
                print("f4.write error")

            # check for weighted accounts and write again to file if true

            faves_by = get_user_ids_of_post_likes(tweet.id)
            if faves_by:
                if any(ext in faves_by for ext in weighted_user_ids):
                    print("found fav by weightened user")
                    try:
                        f2.write(text + "\n")
                    except:
                        print("f2 write error")

            amt_posted += 1

            if amt_posted == max_posts_to_do_at_once:
                break


f3.close()
f2.close()
