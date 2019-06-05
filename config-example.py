# set to 1 to disable online functionality and just generate tweet + picture
test=1

# PATHS

tmp_path ="tmp/"
out_path = "output/"
back_path = "insta-pics/"

script_story = "instagram-php/uploadJJ.php"
script2 = "instagram-php/uploadJJPost.php"

id_file = "id.txt"
printed_tweets_file = "printed.txt"

# CORPUS FILE
corpus_file = "jj-nomention.txt"
chain_file = "jj.json"

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

# TWITTER USER IDS
jj_user_id="878210144827580416"
bot_id = "1067095466175811586"

# MAX AMOUNT OF TWEETS AT ONCE
max_tweet_amount = 3

# REACT TO JJ
retweet_jj = 1
trigger_words = ["bot", "algorith"]

# THRESHOLD TO CROSSPOST TO INSTAGRAM
like_threshold = 1
retweet_threshold = 1

# MAX CHARS PER LINE (INSTAGRAM)
chars_per_line = 15

# INSTAGRAM FONT STYLE
font_file = "fonts/SF-Pro-Display-Semibold.otf"
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
