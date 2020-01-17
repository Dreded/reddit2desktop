#Evan Nguyen
import praw, urllib.request, os, ctypes, datetime, time


def main():
	#create data folder to put the image and txt file 
	dir = os.path.dirname(os.path.realpath(__file__)) + "\\data\\"

	get_image(dir)

def get_image(directory):
	#initialize praw.ini to authenticate the reddit api
	reddit = praw.Reddit('bot', user_agent='reddit2desktop')
	#go to /r/wallpapers/hot
	get_hottest = reddit.subreddit('wallpapers').hot(limit=1)

	#obtain post info
	for post in get_hottest:
		url = post.url
		link = post.permalink
		title = post.title
		author = post.author.name
		#convert date and time to a better format
		date = datetime.datetime.fromtimestamp(post.created)

	#create directories
	dir = directory
	#if data doesnt exist, create one
	if not os.path.exists('data'):
		os.makedirs('data')
	#create the files
	image_directory = directory + 'current_img.jpg'
	text_directory = directory + 'info.txt'

	#retrieve url, download to the directory / output post info to txt file
	urllib.request.urlretrieve(url, image_directory)
	#write to the text file the post information
	with open(text_directory, 'w') as file:
		file.write('Title: ' + title + '\n' + 'https://reddit.com' + link + '\n' + 'Submitted by /u/'+ author + ' on ' + str(date))
	#set wallpaper
	SPI_SETDESKWALLPAPER = 20
	ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_directory, 0)

if __name__ == '__main__':
	main()