#!/bin/bash

# Attempt at parallel ffmpeg converting

for song in *; do
	if [[ $(grep flac "$song") == "" ]]; then
		renamed=${song//.flac/.mp3}
		ffmpeg -i "$song" "$renamed" &
	fi
done

