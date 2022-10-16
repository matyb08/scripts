#!/usr/bin/python3

# Script for downloading shitpost videos

# TODO:
# An OPTION to remove tmp files (if the download was interrupted)
# Enhance logging (also log final filenames)
# Ignore comments (#) in todo file
# Convert if sus file type is downloaded w/ wget
# try: count the number of videos before every new download. If the download succeded and the number of videos is the same, terminate and print the alert (check if os.system() returns any exit codes)
# make the following animation when acknowledging todo: [##############..........................]

import os
import random
import getopt
import sys
import datetime

DIR_PATH = '/main-disk/Goodies/shitpost/'
TODO_PATH = '/main-disk/TMP/shitpost-todo.txt'
LOG_FILE = '/var/log/my-logs/shitpost.log'

# ! UNCOMMENT FOR TESTING !
# DIR_PATH = '/test/'
# TODO_PATH = '/test/shitpost-todo.txt'
# LOG_FILE = '/var/log/my-logs/test-shitpost.log'

# Used only for checking whether to download directly or w/ youtube-dl
VIDEO_FORMATS = ('mp4', 'mkv', 'webm', 'mov', 'avi') # Add more if needed

def write_log(url: str) -> None:
	with open(LOG_FILE, 'a') as log:
		log.write(str(datetime.datetime.now()) + ' | ' + url + '\n')

# If the link already has a file extension
def download_directly(url: str, rand_num: str) -> None:
	write_log(url)
	dot = '.'
	os.system(f'wget \'{url}\' -O \'{DIR_PATH}shitpost-status{rand_num}.{url.split(dot)[-1]}\'')

def regular() -> None:
	while True:
		url = input('PASTE to download, q to quit: ')
		if url == 'q' or url == 'Q':
			exit()

		os.system('clear')

		if url.split('.')[-1] in VIDEO_FORMATS:
			download_directly(url, gen_rand_num())
		else:
			download_w_youtube_dl(url, gen_rand_num())
		
		print()

def the_acknowledging_of_todo() -> None:
	with open(TODO_PATH, 'r+') as todo:
		links = todo.read().split('\n')
		if links[-1] == '':
			links = links[:-1]
		
		for i, link in enumerate(links):
			print(f'Downloading todo... [{i + 1}/{len(links)}]')
			if link.split('.')[-1] in VIDEO_FORMATS:
				download_directly(link, gen_rand_num())
			else:
				download_w_youtube_dl(link, gen_rand_num())

			os.system('clear')

		print('Downloaded todo.')
		todo.truncate(0) # Deletes contents if opened with r+

def download_w_youtube_dl(url: str, rand_num: str) -> None:
	write_log(url)
	os.system('yt-dlp --no-warnings --download-archive \''
				+ DIR_PATH + '.downloaded.txt\''
				+ ' -o \''
				+ DIR_PATH + 'shitpost-status'
				+ rand_num
				+ '.%(ext)s\''
				+ ' -f \'mp4[height=720]+m4a/bestvideo[height<=720]+bestaudio\' --ignore-config --no-playlist '
				+ url)

def gen_rand_num() -> str:
	rand_num = '{0:08}'.format(random.randint(1, 99999999))

	files = os.listdir(DIR_PATH)
	i = 0
	while i < len(files):
		if rand_num in files[i]:
			rand_num = '{0:08}'.format(random.randint(1, 99999999))
			i = 0

		else:
			i += 1
	
	return rand_num	

def parse() -> bool:
	options, arguments = getopt.getopt(
		sys.argv[1:],
		's', # 's:' if it requires an argument
		['skip-todo']
	)

	skip_todo = False
	for o, a in options:
		if o in ('-s', '--skip-todo'):
			skip_todo = True
	
	return skip_todo
		

if __name__ == '__main__':
	os.system('clear')

	if not (os.stat(TODO_PATH).st_size == 0) and not parse():
		the_acknowledging_of_todo()
		regular()
	else:
		regular()

