from config import *
from print_quote import *
from clean_tweet import clean_tweet

import markovify
import sys
import re
import random
from random import randint
import tweepy


def generate_quote(starts_with=None):
    # create text model
    k = randint(markov_state_size_range[0], markov_state_size_range[1])
    text_model = markovify.NewlineText(corpus_text, state_size=k)
    tweet = None
    length = randint(min_length, max_length)
    overlap = random.uniform(min_overlap, max_overlap)
    if starts_with is None:
        while tweet is None:
            tweet = text_model.make_short_sentence(
                length, max_overlap_ratio=overlap)
    else:
        while tweet is None:
            tweet = text_model.make_sentence_with_start(
                starts_with, strict=False, max_words=length, max_overlap_ratio=overlap)

    return tweet


def post_tweet(text, answer_id=None):
    if answer_id:
        api.update_status(text, tweet.id)
        api.create_favorite(tweet.id)
    else:
        api.update_status(text)
    # clean up text and add to archive
    text = clean_tweet(text)
    f = open(corpus_file, "a")
    f.write(text.encode('utf-8') + "\n")
    f.close()
    try:
        f2.write(text.encode('utf-8') + "\n")
    except:
        print("f2.write error")  


def check_jj_tweets():
    print("reading tweets")
    tweets = api.user_timeline(user_id=jj_user_id, count=20,
                               tweet_mode='extended',  include_rts=1, since_id=last_id)

    for tweet in tweets:

        # interact with jj tweets

        if react_to_jj:

            # check for trigger words
            if tweet.in_reply_to_screen_name is None:
                reply_check = "none"
            else:
                reply_check = tweet.in_reply_to_screen_name

            if any(ext in tweet.full_text for ext in trigger_words) or \
                    any(ext in reply_check for ext in trigger_words):

                print("Answering to tweet by " + tweet.user.screen_name + 
                        " in reply to " + reply_check + ":" + tweet.full_text)

                # weighted random: whether to start answer with defined words
                rand_sel = randint(0, 5)
                if rand_sel == 0:
                    answer = generate_quote("du")
                elif rand_sel == 1:
                    answer = generate_quote("ich")
                else:
                    answer = generate_quote()

                answer = "@sickbutsocial " + answer

                if send_tweets:
                    post_tweet(answer, tweet.id)

    # save id of last checked tweet
    if len(tweets) > 0:
        f = open(id_file, "w")
        f.write(str(tweets[0].id))
        f.close()


def check_mentions():
    print("reading mentions")
    tweets = api.mentions_timeline(
        user_id=bot_id, count=10, tweet_mode='extended',  include_rts=1, since_id=last_id_mentions)
    print("found " + str(len(tweets)) + " mentions")

    for tweet in tweets:

        # interact with mentions other than my own
        print("Mentioned by " + tweet.user.screen_name + 
              " / " + tweet.user.id_str + " :" + tweet.full_text)
        if react_to_mentions == 1 and tweet.user.id_str != bot_id:
            print("Reacting to tweet")

            # weighted random: whether to start answer with defined words
            rand_sel = randint(0, 3)
            if rand_sel == 0:
                answer = generate_quote("du")
            else:
                answer = generate_quote()

            answer = "@" + tweet.user.screen_name + " " + answer

            if send_tweets:
                post_tweet(answer, tweet.id)

    # save id of last checked tweet
    if len(tweets) > 0:
        f = open(id_mentions_file, "w")
        f.write(str(tweets[0].id))
        f.close()


if __name__ == "__main__":

    # LOAD CORPUS TEXT FILE
    with open(corpus_file) as f:
        corpus_text = f.read()

    # TWITTER LOGIN
    if check_tweets:
        print("logging in")
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        api = tweepy.API(auth)
        print("logged in")
        print("my id: " + bot_id)

    # SET AMOUNT OF TWEETS TO GENERATE
    j = randint(1, max_tweet_amount)

    # open files to write to
    f = open(corpus_file, "a")
    f2 = open(archive_file, "a+")

    # GENERATE TWEETS
    i = 0
    while i < j:
        tweet = generate_quote()

        if send_tweets:
            post_tweet(tweet)

        else:
            # we're offline -> only output the tweet
            print(tweet)
            main_print_function(tweet, story=False, post=False)
        i += 1

    f.close()

    # INTERACT WITH TWEETS
    if check_tweets:

        # check last checked tweet id
        if os.path.exists(id_file):
            f = open(id_file, "r+")
            last_id = f.readline()
            f.close()
        else:  # if none: create last checked file
            f = open(id_file, "w+")
            f.write(str(0))
            last_id = 1000
            f.close()

        if os.path.exists(id_mentions_file):
            f = open(id_mentions_file, "r+")
            last_id_mentions = f.readline()
            f.close()
        else:
            f = open(id_mentions_file, "w+")
            f.write(str(0))
            last_id_mentions = 1000
            f.close()

        check_jj_tweets()
        check_mentions()
