### sickbotsocial
______

[logo]: http://www.dieyungenhuren.hiv/sickbotsocial/ava.jpg "sickbotsocial"

[www.dieyungenhuren.hiv](http://www.dieyungenhuren.hiv/)

[twitter](http://www.twitter.com/sickbotsocial/) | 
[instagram](http://www.instagram.com/sickbotsocial/) |
[image archive](http://www.dieyungenhuren.hiv/sickbotsocial/img/e)

twitter bot that generates quotes in the style of [Jessica Jurassica](http://www.twitter.com/sickbutsocial/). any user interaction with the tweets by this bot will make him crosspost them to instagram with a picture taken and edited from JJs insta-feed.

______

#### config:
online functionality (reading new tweets, tweeting, crossposting to instagram) is disabled in config (set `test=0` to enable). twitter API keys, and an instagram account is necessary for these features.

- clone github repo
- install requirements `pip install -r requirements.txt`
- setup `config.py` file (edit and rename `config-example.py`)
- add .jpg images to folder `insta-pics/`
- run `python jj-quote.py`

#### modules:
- `jj-quote.py` - *main*
- `tw_favs_to_insta.py` - *checks for twitter interaction & triggers image generation*
- `print_quote.py` - *overlays quote on image file*

________

#### python requirements: 
- `tweepy==3.6.0`
- `markovify==0.7.1`
- `Pillow==6.0.0`

#### additional requirements for instagram functionality
- [Instagram PHP](https://github.com/mgp25/Instagram-API) (clone into folder instagram-php and setup `config.php` file)

