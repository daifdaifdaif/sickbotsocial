### sickbotsocial
```
it girl bot ///////// / 
underground literatin / kunstfigur ///////// ///////// 
virtual art performance ///////// 
```

[logo]: http://www.dieyungenhuren.hiv/sickbotsocial/ava.jpg "sickbotsocial"

[www.dieyungenhuren.hiv](http://www.dieyungenhuren.hiv/)

[twitter](http://www.twitter.com/sickbotsocial/) | 
[instagram](http://www.instagram.com/sickbotsocial/) |
[image archive](http://www.dieyungenhuren.hiv/sickbotsocial/img/)

twitter bot that generates tweets in the style of [Jessica Jurassica](http://www.twitter.com/sickbutsocial/) using markov-chains. any user interaction with the tweets by this bot will make him crosspost them to instagram with a picture taken and edited from JJs insta-feed.

______

#### modules:
- `jj-quote.py` - *main*
- `tw_favs_to_insta.py` - *checks for twitter interaction & triggers image generation*
- `print_quote.py` - *overlays quote on image file*

_________


#### config & usage:
multiple parameters can be edited in `config.py`. online functionality (reading new tweets, tweeting, crossposting to instagram) is disabled per default (set `test=0` to enable). twitter API keys and an instagram account are necessary for these features. the supplied corpus file isn't up to date (27.11.18), please pull all the newer Jessica Jurassica tweets by yourself.

1. clone github repo
2. run install: `python setup.py install`
3. setup `config.py` file (add path to font file `font_file=""`)
4. *add .jpg images to folder `insta-pics/` (optional)*
5. run `cd sickbotsocial && python jj-quote.py`

quotes are output in terminal. created image files are found in the `output` directory.

_________


#### python requirements: 
runs on python 2.7

- [`tweepy==3.6.0`](https://github.com/tweepy/tweepy)
- [`markovify==0.7.1`](https://github.com/jsvine/markovify/)
- [`Pillow==6.0.0`](https://github.com/python-pillow/Pillow)

#### additional requirements for instagram functionality
- [`Instagram API`](https://github.com/mgp25/Instagram-API) (clone into folder instagram-php and setup `config.php` file)

