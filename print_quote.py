#!/bin/python
# -*- coding: utf-8 -*-

import textwrap
import random

from config import *

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
test=0
hard_test=0
chain_file = "/home/pi/jj-bot/jj.json"


x = 50
y = 30


# setup
tmp_path ="/home/pi/jj-bot/tmp/"
out_path = "/home/pi/jj-bot/output/"
back_path = "/home/pi/jj-bot/insta-pics/"

script_story = "/home/pi/jj-bot/instagram-php/uploadJJ.php"
script2 = "/home/pi/jj-bot/instagram-php/uploadJJPost.php"





def mixup_img(img):
	img = ImageEnhance.Brightness(img).enhance(0.9)
	if random.random() < rotate:
		print("rotate image")
		x = random.random()
		if x < 0.3:
			img = img.rotate(90)
		elif x > 0.7:
			img = img.rotate(180)
		else:
			img = img.rotate(270)
	
	if random.random() < brighten:
		print("brighten image")
		img = ImageEnhance.Brightness(img).enhance(1.1)
	
	if random.random() < darken:
		print("darken image")
		img = ImageEnhance.Brightness(img).enhance(0.9)
		
	if random.random() < mirror:
		print("flip image")
		img = img.transpose(Image.FLIP_LEFT_RIGHT)
		
	if random.random() < crop:
		print("zoom image")
		w = random.randint(100,450)
		h = random.randint(650,1000)
		img.crop((w,w,h,h))
		img = img.resize((1080,1080))
		
	return(img)


def print_quote(s, template_file, story=True, font_size=90):

	print "\nprint_quote()"
	print "quote to print: " + s
	
	if len(s) <= 1:
		return False
	
	ts = time.time()
	st = datetime.fromtimestamp(ts).strftime('%Y%m%d_%H%M%S')

	
	random.seed(time.clock())
	print "Chosen template: " + template_file
	

	s = s.decode('utf-8')
	s = s.lower()
	
	s = re.sub(r'[&].+\s', '', s)
	
	if len(s) > 100:
		if len(s) > 250:
			font_size = font_size - 50
		elif len(s) > 200:
			font_size = font_size - 40
		elif len(s) > 150:
			font_size = font_size - 30
		else:
			font_size = font_size - 20
			
		print("long quote detected")
	
	font = ImageFont.truetype("/home/pi/fonts/SF-Pro-Display-Semibold.otf", font_size, encoding="unic")
	
	
	content = textwrap.wrap(s, width=chars_per_line,break_long_words=False)
	
	
	img = Image.open(template_file)
	img = mixup_img(img)
	draw = ImageDraw.Draw(img)

	# draw wrapped text
	y2 = y
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
	
	# more jpg
	img = img.resize((800,800))
	img = img.resize((1080,1080))
	img = img.filter(ImageFilter.SMOOTH)
	
	# create files
	if story:
		img2 = Image.new("RGB", (1080,1920), color = 'white')
		img2.paste(img, (0,420))
		img2.save(out_file_story)

	img.save(out_file)


	return out_file, out_file_story, out_file_name




# load background files 

def main_printer(tweet=None, story=True, post=False):

	
	# choose template file
	template_files = []
	listOfFiles = os.listdir(back_path) 
	for entry in listOfFiles:
		template_files.append(back_path + entry)

	template_file = template_files[random.randint(1,(len(template_files)-1))]
	
	# open ftp session
	try:
		session = ftplib.FTP(HOST,USER,PASSWD)
	except:
		print("FTP failure")


	# check whether text was provided 
	# generate text if not
	if tweet == None:


		print("reading corpus: "+corpus_file)
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
		

	print(tweet)

	# create image
	if not hard_test:
		file, file_story, file_name = print_quote(tweet, template_file);


	# post
	if not test and not hard_test:	
		
		# write temporary file with description for apache index list
		tmp_file_path = tmp_path + "tmp.txt"
		tmp_file = open(tmp_file_path,'w+')
		tmp_file.write('AddDescription \'<a href="'+file_name+'.jpg'+'">'+tweet+'</a>\' ' + file_name +'.jpg' + '\n')
		tmp_file.close()
		
		# ftp upload
		try:
			ftp_file = open(file,'rb')
			session.storbinary('STOR '+file_name+'.jpg', ftp_file)  
			ftp_file.close()
			ftp_file = open(tmp_file_path,'rb')
			session.storbinary('APPE .htaccess', ftp_file)
			ftp_file.close()  
			
		except:
			print("ftp failure")
		
		if story:
			os.system("php7.0 " + script_story + " "+ file_story + "> /dev/null")
		if post:
			os.system("php7.0 " + script2 + " "+ file + " \""+ tweet +" #sickbotsocial #dieyungenhurendothiv\" > /dev/null")
		

	
	
	session.quit()
	
	print("Finished")


if __name__ == "__main__":
    main_printer()
