#!/bin/python
# -*- coding: utf-8 -*-

import textwrap
import random

from config import *
from clean_tweet import clean_tweet

import re, time
from datetime import datetime, timedelta

import os
import sys

import ftplib

from PIL import Image, ImageFont, ImageDraw, ImageFilter, ImageEnhance


import re

import markovify
import json
import sys
import re

import random
from random import randint


# GLOBALS
hard_test=0

# font coordinates
x = 50
y = 30


# FUNCTION: REMIX IMAGE (crop, rotate, brighten, ....)

def mixup_img(img):
	img = ImageEnhance.Brightness(img).enhance(0.9)
	if random.random() < rotate:
		x = random.random()
		if x < 0.3:
			img = img.rotate(90)
		elif x > 0.7:
			img = img.rotate(180)
		else:
			img = img.rotate(270)
	
	if random.random() < brighten:
		img = ImageEnhance.Brightness(img).enhance(1.1)
	
	if random.random() < darken:
		img = ImageEnhance.Brightness(img).enhance(0.9)
		
	if random.random() < mirror:
		img = img.transpose(Image.FLIP_LEFT_RIGHT)
		
	if random.random() < crop:
		w1 = random.randint(100,450)
		w2 = random.randint(100,450)
		h1 = random.randint(650,1000)
		h2 = random.randint(650,1000)
		img.crop((w1,w2,h1,h2))
		img = img.resize((1080,1080))
	
	return(img)


# FUNCTION: DRAW TWEET ON IMAGE
# s = string to print
# template_file = path to background Image
# story = whether to create 1080 * 1920 version of image

def print_quote(s, template_file, story=True, font_size=90):
	
	if len(s) <= 1:
		return False

	# get timestamp to generate filename
	ts = time.time()
	st = datetime.fromtimestamp(ts).strftime('%Y%m%d_%H%M%S')

	# clean up text
	s = s.decode('utf-8')
	s = s.lower()
	s = clean_tweet(s)
	
	# adjust font size to text length
	if len(s) > 100:
		if len(s) > 250:
			font_size = font_size - 50
		elif len(s) > 200:
			font_size = font_size - 40
		elif len(s) > 150:
			font_size = font_size - 30
		else:
			font_size = font_size - 20
	
	# wrap text
	content = textwrap.wrap(s, width=chars_per_line,break_long_words=False)
				
	# load font
	try:
		font = ImageFont.truetype(font_file, font_size, encoding="unic")
	except:
		print("error loading font. check config.py and edit font_file path")
		sys.exit()
	
	# load & remix image
	img = Image.open(template_file)
	img = mixup_img(img)
	
	# begin drawing
	draw = ImageDraw.Draw(img)

	# draw wrapped text
	# y = font coordinate
	y2 = y
	
	# loop through to create outlines
	for text in content:
		draw.text((x-outline, y2-outline), text,outline_color,font=font)
		draw.text((x+outline, y2-outline), text,outline_color,font=font)
		draw.text((x+outline, y2+outline), text,outline_color,font=font)
		draw.text((x-outline, y2+outline), text,outline_color,font=font)
		draw.text((x, y2), text, text_color, font)
		y2 = y2 + font_size + 5

	# set out files
	out_file_name = st
	out_file = out_path + out_file_name + ".jpg"
	out_file_story = out_path + "story.jpg"
	
	# add more jpg
	img = img.resize((850,850))
	img = img.resize((1080,1080))
	img = img.filter(ImageFilter.SMOOTH)
	
	# create files to post
	if story:
		img2 = Image.new("RGB", (1080,1920), color = 'white')
		img2.paste(img, (0,420))
		img2.save(out_file_story)
	img.save(out_file)
	print("created image: " + out_file)

	return out_file, out_file_story, out_file_name


# FUNCTION: SELECT BACKGROUND IMAGE FROM IMAGE CORPUS
def choose_background():

	# check which images have been used
	f = open(printed_imgs_file, "rw+")
	used_files = f.readlines()
	
	# reset used images every 300 images
	if len(used_files) > 300:
		f.close()
		f = open(printed_imgs_file, 'w')
		used_files = ["empty"]


	# good random seed
	t = int( time.time() * 1000.0 )
	random.seed( ((t & 0xff000000) >> 24) +
             ((t & 0x00ff0000) >>  8) +
             ((t & 0x0000ff00) <<  8) +
             ((t & 0x000000ff) << 24)   )
	
	
	# load template files
	try:
		template_files = []
		listOfFiles = os.listdir(back_path) 
		for entry in listOfFiles:
			if entry.endswith(".jpg"):
				template_files.append(back_path + entry)
	except:
		print("failure loading template files. check specified directory in config.py")
	

	# if none available make black file
	if not template_files:
		img = Image.new('RGB', (800,800), (255, 255, 255))
		img_path = back_path+"black.jpg"
		img.save(img_path, "JPEG")
		return img_path
	else:
		#select random template file
		while True:
			chosen_image = template_files[random.randint(0,(len(template_files)-1))]
			
			# check if file has been used already
			if (chosen_image + "\n") not in used_files:
				f.write(chosen_image+"\n")
				f.close()
				return chosen_image
	


# MAIN FUNCTION
# gets called by tw_favs_to_insta.py
# tweet = text to print
# story = whether to post to story & create 1080*1920 image
# post = whether to create instagram post

def main_printer(tweet=None, story=True, post=False):

	# check whether text was provided 
	# generate text if not
	if tweet == None:

		print("no text supplied. generating tweet")
		with open (corpus_file) as f:
			text = f.read()

		f.close();



		k = randint(1,3)	
		text_model = markovify.NewlineText(text, state_size=k)


		# TRY TO GENERATE
		tweet = None
		while tweet == None:
			length = randint(min_length,max_length)
			overlap = random.uniform(min_overlap,max_overlap)
			tweet = text_model.make_short_sentence(length,max_overlap_ratio=overlap)
		
		print("tweet: "+tweet)

		
	template_file = choose_background()
	# create image
	if not hard_test:
		file, file_story, file_name = print_quote(tweet, template_file);


	# UPLOAD
	if not test and not hard_test:	

		# APACHE DIRECTORY PREP
		
		# write temporary file with description for apache index list
		tmp_file_path = tmp_path + "tmp.txt"
		tmp_file = open(tmp_file_path,'w+')
		apache_string = clean_tweet(tweet)
		tmp_file.write('AddDescription \'<a href="'+file_name+'.jpg'+'">'+apache_string+'</a>\' ' + file_name +'.jpg' + '\n')
		tmp_file.close()
		
		# FTP UPLOAD
		try:
			session = ftplib.FTP(HOST,USER,PASSWD)
			ftp_file = open(file,'rb')
			session.storbinary('STOR '+file_name+'.jpg', ftp_file)  
			ftp_file.close()
			ftp_file = open(tmp_file_path,'rb')
			session.storbinary('APPE .htaccess', ftp_file)
			ftp_file.close()  
			session.quit()			
		except:
			print("ftp failure")
			
		# INSTA UPLOAD
		
		if story:
			os.system("php7.0 " + script_story + " "+ file_story + "> /dev/null")
		if post:
			os.system("php7.0 " + script2 + " "+ file + " \""+ tweet +" #sickbotsocial #dieyungenhurendothiv\" > /dev/null")
		


if __name__ == "__main__":
    main_printer()
