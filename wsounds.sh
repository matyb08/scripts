#!/bin/bash

# Wholesome sounds downloader

# TODO:
# download from todo file

DIR_PATH="/main-disk/Goodies/wholesome-sounds/"
LOG_PATH="/var/log/my-logs/wholesome-sounds.log"

clear
read -p "Paste link to download the sound, q to quit: " link

while [ true ]
do
	if [[ $link == "q" || $link == "Q" ]]
	then
		break
	else
		clear
		yt-dlp --extract-audio --audio-quality 0 --audio-format "mp3" --ignore-errors --add-metadata --download-archive "$DIR_PATH"".downloaded.txt" --no-post-overwrites --embed-thumbnail --no-playlist --output "$DIR_PATH""%(title)s.%(ext)s" "$link"
		time=$(date --rfc-3339=ns)
		echo "$time | $link" >> $LOG_PATH # btw printf does not add a new line at the end
		printf "\n\n"
		read -p "Paste link to download the sound, q to quit: " link
	fi
done
