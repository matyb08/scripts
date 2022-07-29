#!/bin/sh

# Download single tracks or whole playlists in best sound quality
# ALL OF THE ASSOCCIATED SCRIPTS (fix-album-art.py) OR THE WHOLE SCRIPTS FOLDER (even better), MUST BE ADDED TO PATH

LINK=$1

yt-dlp --extract-audio --audio-quality 0 --audio-format "mp3" --ignore-errors --add-metadata --no-post-overwrites --embed-thumbnail --download-archive ".downloaded.txt" --output "+%(title)s %(id)s.%(ext)s" "$LINK"
fix-album-art.py .
