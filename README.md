### sickbotsocial
```
it girl bot ///////// / 
underground literatin / kunstfigur ///////// ///////// 
virtual art performance ///////// 
```

[logo]: http://www.dieyungenhuren.hiv/sickbotsocial/ava.jpg "sickbotsocial"

[www.dieyungenhuren.hiv](http://www.dieyungenhuren.hiv/)

[twitter](http://www.twitter.com/sickbotsocial/) | 
[instagram](http://www.instagram.com/sickbotsocial/)

*searchable archive of generated tweets and images: [images](http://www.dieyungenhuren.hiv/sickbotsocial/img/) | [tweets](http://www.dieyungenhuren.hiv/sickbotsocial/txt/)*

______

twitter bot that generates tweets in the style of [Jessica Jurassica](http://www.twitter.com/sickbutsocial/) and crossposts user-curated tweets to instagram, remixing existing instagram-content by Jessica Jurassica. it's designed to slowly replace Jessica Jurassica on social media.

it generates tweets by markov-chains, its corpus constisting of all of Jessica Jurassicas tweets and all of its own, previously generated tweets as well. therefore, after ~10k tweets, it started to emancipate itself from its influence and recursively became its own inspiration. twitter-users, who interact with the tweets of this bot, act as curators: if any tweet gets a predifined amount of "attention", it will get crossposted to instagram. the previous instagram-posts of Jessica Jurassica serve as an image library, which gets transformed and remixed, and then used as backgrounds for the tweets.

______
`the implementation of the instagram API in this repository is broken. the bot locally runs using instagram-private-API now. I suggest taking a look at instagram-private-api, if you want to copy this project. text- or twitter-only implementation is still possible with this repository, image generation as well.`
______

#### executable modules:
- `jj-quote.py` - *main*
- `print_quote.py` - *overlays quote on image file*

#### executable scripts:
- `tw_favs_to_insta.py` - *checks for twitter interaction & triggers image generation*

#### helper modules:
- `clean_tweet.py` - *regex clean up, removes mentions, "RT" etc*

_________


#### config & usage:
multiple parameters can be edited in `config.py`. online functionality (reading new tweets, tweeting, crossposting to instagram) is disabled per default (set first three variables in `config.py` to change this). twitter API keys and an instagram account are necessary for these features. the supplied corpus file isn't up to date (27.11.18), please pull all the newer Jessica Jurassica tweets by yourself or use twitter API key and let `tw_favs_to_insta.py` pull the tweets for you.

1. clone github repo
2. run install: `python setup.py install`
3. setup `config.py` file (add path to font file `font_file=""`)
4. *add .jpg images to folder `insta-pics/` (optional)*
5. run `python sickbotsocial/jj-quote.py`

if online functionality is disabled, quotes are directly output in the terminal window. created image files are found in the `output` directory.

_________


#### python requirements: 
runs on python 2.7

- [`tweepy==3.6.0`](https://github.com/tweepy/tweepy)
- [`markovify==0.7.1`](https://github.com/jsvine/markovify/)
- [`Pillow==6.0.0`](https://github.com/python-pillow/Pillow)


#### additional tools:
- [`instaloader`](https://instaloader.github.io/) (used to update library of instagram pics)

_________

written by DAIF & Jessica Jurassica, 2019-2021. #dieyungenhurendothiv
