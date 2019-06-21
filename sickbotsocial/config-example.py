# set to 1 to disable online functionality and just generate tweet + picture
test=1

# PATHS

tmp_path ="../tmp/"
out_path = "../output/"
back_path = "../insta-pics/"

script_story = "../instagram-php/uploadJJ.php"
script2 = "../instagram-php/uploadJJPost.php"

id_file = "../tmp/id.txt"
printed_tweets_file = "../printed.txt"

# CORPUS FILE
corpus_file = "../corpus/jj-nomention.txt"
chain_file = "../corpus/jj.json"

# TWEET LENGTH
min_length=30
max_length=230

# TWEET LENGTH FOR ANSWERS
# (must be specified seperately for markovify)
min_words=5
max_words=20

# MARKOV PARAMETERS
min_overlap=0.35
max_overlap=0.85
markov_state_size_range=[1,3]

# TWITTER USER IDS
jj_user_id="878210144827580416"
bot_id = "1067095466175811586"

# TWITTER USER IDS WITH DOUBLE WEIGTH
# if these users fav bot tweets the tweets get added to the corpus double weighted
weighted_user_ids = [jj_user_id, bot_id, "906895118912901121"]

# MAX AMOUNT OF TWEETS AT ONCE
max_tweet_amount = 2

# REACT TO JJ
retweet_jj = 1
retweet_myself = 1
trigger_words = ["bot", "algorith"]

# THRESHOLD TO CROSSPOST TO INSTAGRAM
like_threshold = 1
retweet_threshold = 1

# MAX CHARS PER LINE (INSTAGRAM)
chars_per_line = 15

# INSTAGRAM FONT STYLE
font_file = "/Library/Fonts/Arial.ttf"
outline = 1
outline_color = (255,255,255)
text_color = (255,255,255)
text_color2 = (0,0,0)

# INSTAGRAM MASHUP THRESHOLD
rotate = 0.2
brighten = 0.1
crop = 0.6
darken = 0.2
mirror = 0.2

# add ftp host to upload generated images
HOST=''
USER=''
PASSWD=''

# twitter API key
consumer_key = ""
consumer_secret = ""
access_token = ""
access_secret = ""
