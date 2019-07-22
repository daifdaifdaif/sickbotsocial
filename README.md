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

twitter bot that generates tweets in the style of [Jessica Jurassica](http://www.twitter.com/sickbutsocial/) using markov-chains. any user interaction with the tweets by this bot will make him crosspost them to instagram with a picture taken and edited from JJs insta-feed.

*a short description of the ideas behind this project are found in german [here](SAALTEXT.md)*.

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

#### additional requirements for instagram functionality:
- [`Instagram API`](https://github.com/mgp25/Instagram-API) (clone into folder instagram-php, update config.py with paths and enter credentials)

