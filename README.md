# jj-bot

needs:
* config.py file 
* instagram-php/config.php file
* .jpg images in folder insta-pics/

jj-quote.py -> main generator

tw_favs_to_insta.py -> checks for favs & RTs, launches print_quote.py & uploads to insta

print_quote.py -> overlays quote on image file 


## config.py file (_rename & edit config-example.py_)
```
# ftp credentials for automated uploading
HOST=''
USER=''
PASSWD=''

# twitter api keys
consumer_key = ""
consumer_secret = ""
access_token = ""
access_secret = ""
```

## instagram.php/config.php file (_rename & edit config-example.php_)
instagram credentials:
```
<?php
$username = '';
$password = '';
?>
```
