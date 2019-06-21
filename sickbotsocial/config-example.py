# set to 1 to disable online functionality and just generate text + picture
run_offline=1

#############
### PATHS ###
#############

tmp_path ="../tmp/"
out_path = "../output/"
back_path = "../insta-pics/"

# php scripts to upload to insta
script_story = "../instagram-php/uploadJJ.php"
script2 = "../instagram-php/uploadJJPost.php"

# to save which tweets already got read
id_file = "../tmp/id.txt"

# to save which tweets got crossposted and which images used to print them
printed_tweets_file = "../printed.txt"
printed_imgs_file = "../insta-pics/printed_imgs.txt"

#######################
### TWITTER OPTIONS ###
#######################

# MAX AMOUNT OF TWEETS AT ONCE
max_tweet_amount = 2

# twitter user ids
jj_user_id="878210144827580416"
bot_id = "1067095466175811586"

# twitter user ids for double weighted saving tweets
# if these users fav bot tweets they get added to the corpus double weighted
weighted_user_ids = [jj_user_id, bot_id, "906895118912901121"]

# REACT TO TWEETS
retweet_jj = 1
retweet_myself = 1
trigger_words = ["bot", "algorith"]

###############################
### TEXT GENERATION OPTIONS ###
###############################

# CORPUS FILES
# these get written to by the bot with its own tweets
corpus_file = "../corpus/jj-nomention.txt"
chain_file = "../corpus/jj.json"

# TWEET LENGTH
min_length=30
max_length=230

# UNUSED TWEET LENGTH
min_words=5
max_words=20

# MARKOV PARAMETERS
min_overlap=0.35
max_overlap=0.85
markov_state_size_range=[1,3]

#####################
### IMAGE OPTIONS ###
#####################

# FONT STYLE
font_file = "/Library/Fonts/Arial.ttf"
outline = 1
outline_color = (255,255,255)
text_color = (255,255,255)
text_color2 = (0,0,0)

# MAX CHARS PER LINE
chars_per_line = 15

# CHANCE TO MASHUP IMAGE
rotate = 0.2
brighten = 0.1
crop = 0.6
darken = 0.2
mirror = 0.2

# LIKES OR RETWEETS NEEDED TO CROSSPOST TO INSTAGRAM
like_threshold = 2
retweet_threshold = 1

# MAX INSTA POSTS TO DO AT ONCE
max_posts_to_do_at_once = 2

########################
### API/CREDENTIALS  ###
########################


# add ftp host to upload generated images
HOST=''
USER=''
PASSWD=''

# twitter API key
consumer_key = ""
consumer_secret = ""
access_token = ""
access_secret = ""
