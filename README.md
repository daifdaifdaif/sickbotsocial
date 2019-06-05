### sickbotsocial
______

[logo]: http://www.dieyungenhuren.hiv/sickbotsocial/ava.jpg "sickbotsocial"

[www.dieyungenhuren.hiv/sickbotsocial/](http://www.dieyungenhuren.hiv/sickbotsocial)

[twitter](www.twitter.com/sickbotsocial/) | 
[instagram](www.instagram.com/sickbotsocial/) |
[image archive](www.dieyungenhuren.hiv/sickbotsocial/img/e)

twitter bot that generates quotes in the style of [Jessica Jurassica](http://www.twitter.com/sickbutsocial/). any user interaction with the tweets by this bot will make him crosspost them to instagram with a picture taken and edited from JJs insta-feed.

______

#### config:
online functionality (reading new tweets, tweeting, crossposting to instagram) is disabled in config (set `test=0` to enable). twitter API keys, and an instagram account is necessary for these features.

- setup `config.py` file (edit&rename `config-example.py`)
- add .jpg images to folder `insta-pics/`
- run `python jj-quote.py`

#### python requirements: 
- `tweepy==3.6.0`
- `markovify==0.7.1`
- `Pillow==6.0.0`

#### additional requirements for instagram functionality
- [Instagram PHP==6.0.1](https://github.com/mgp25/Instagram-API) (clone into folder instagram-php and setup `instagram-php/config.php` file)

#### modules:
- `jj-quote.py` - *main generator*
- `tw_favs_to_insta.py` - *checks for twitter interaction & triggers image generation*
- `print_quote.py` - *overlays quote on image file*
