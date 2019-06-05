## sickbotsocial

[www.dieyungenhuren.hiv/sickbotsocial/](http://www.dieyungenhuren.hiv/sickbotsocial)

twitter bot that generates quotes in the style of [Jessica Jurassica](http://www.twitter.com/sickbutsocial/). any user interaction with the tweets by this bot will make him crosspost them to instagram with a picture taken and edited from JJs insta-feed.

has to be run periodically (e.g. once per hour via crontab).


#### installation:
- setup `config.py` file (edit&rename `config-example.py`)
- setup `instagram-php/config.php` file (edit&rename `config-example.php`)
- add .jpg images to folder `insta-pics/`
- run `python jj-quote.py`

#### requirements: 
- `tweepy==3.6.0`
- `markovify==0.7.1`
- `Pillow==6.0.0`

#### modules:
- `jj-quote.py` - *main generator*
- `tw_favs_to_insta.py` - *checks for twitter interaction & triggers image generation*
- `print_quote.py` - *overlays quote on image file *
