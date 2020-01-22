#!/usr/bin/python

'''
Original Code by Evan Ngyun edited by Dreded for Linux users and multiple subs
This script picks a reddit sub from wallpapersubs list and then sets it as the desktop background

It chooses the image from the top 10 hot submissions in the sub(only checks the top 10 in 1 sub)
Please Note it only downloads 1 image per run.

Works in Windows and Linux if using KDE Plasma as DM
'''

import subprocess
import praw
import urllib.request
import os
import ctypes
import datetime
import time
import platform
import random
import time
import configparser

def getConfig():
	rootpath = os.path.dirname(os.path.realpath(__file__))
	dir = os.path.join(rootpath,'data')

	if not os.path.exists('data'):
		os.makedirs('data')
  
	config = configparser.ConfigParser()
	configFileLocation = os.path.join(rootpath,'reddit2desktop.config.example')
	config.read(configFileLocation)

	configDict = {}
	section = 'configuration'
	options = config.options(section)

	for option in options:
		try:
			configDict[option] = config.get(section, option)
			if configDict[option] == -1:
				DebugPrint("skip: %s" % option)
		except:
			print("exception on %s!" % option)
			configDict[option] = None
	configDict.update({'directory': dir})
	return configDict



def applyBackground(config):
    #get some more config options(these two are added after config file is parsed)
	bgimage = config['bgimage']
	title = config['postTitle']
	randomsub = config['randomsub']
	my_platform = platform.system()

	if config['verbose']:
		print('Platform:',my_platform)
		print('Setting background to:',bgimage)
		print('Wallpaper from Sub:',randomsub)
		print('Title of Post:',title)
  
	if my_platform == 'Windows':
		SPI_SETDESKWALLPAPER = 20
		ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, bgimage, 0)
		
	elif my_platform == 'Linux':
		#set wallpaper
		command = ['qdbus', 'org.kde.plasmashell', '/PlasmaShell', 'org.kde.PlasmaShell.evaluateScript']
		command.append("""
			var allDesktops = desktops();
			for (i=0;i<allDesktops.length;i++)
			{{
				d = allDesktops[i];
				d.wallpaperPlugin = "org.kde.image";
				d.currentConfigGroup = Array("Wallpaper", "org.kde.image", "General");
				d.writeConfig("Image", "file://{}");
			}}
			""")

		command[-1] = command[-1].format(bgimage)
		subprocess.run(command)

	else:
		print("Sorry unsupported OS: {}".format(platform.system()))
		exit()

def main():
	config = getConfig()
	get_image(config)
	applyBackground(config)

def get_image(config):
    #get config parameters needed to download image
	directory = config['directory']
	saveAllImages = config['save_all_images']
	my_client_id = config['my_client_id']
	my_client_secret = config['my_client_secret']
	subs = config['subs'].split(',')
	randomsub = random.choice(subs)
 
	#set file locations
	timestr = time.strftime("%Y%m%d-%H%M%S")
	if saveAllImages:
		image_directory = os.path.join(directory,timestr+'.jpg')
		text_directory = os.path.join(directory,timestr+'.txt')
	else:
		image_directory = os.path.join(directory,'currentBG.jpg')
		text_directory = os.path.join(directory,'info.txt')

	#initialize praw
	reddit = praw.Reddit(client_id=my_client_id,client_secret=my_client_secret, user_agent='reddit2desktop')
	post = list(reddit.subreddit(randomsub).hot(limit=10))[random.randrange(10)]

	#obtain post info
	url = post.url
	link = post.permalink
	title = post.title
	author = post.author.name
	date = datetime.datetime.fromtimestamp(post.created)

	#retrieve url, download to the directory / output post info to txt file
	urllib.request.urlretrieve(url, image_directory)
	with open(text_directory, 'w') as file:
		file.write('Title: ' + title + '\n' + 'https://reddit.com' + link + '\n' + 'Submitted by /u/'+ author + ' on ' + str(date))
	config.update({'postTitle': title})
	config.update({'bgimage': image_directory})
	config.update({'randomsub': randomsub})
	return config

if __name__ == '__main__':
	main()
 