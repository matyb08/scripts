#!/bin/sh

# Update my YouTube music playlists
# ALL OF THE ASSOCCIATED SCRIPTS (fix-album-art.py) OR THE WHOLE SCRIPTS FOLDER (even better), MUST BE ADDED TO PATH

# 'The Playlist'
THE_PLAYLIST_PLAYLIST=$(echo $THE_PLAYLIST_PLAYLIST_YOUTUBE)
THE_PLAYLIST_DIR_PATH="/main-disk/Goodies/Music/The Playlist/"

# 'Not Current Pop' (OG, i know)
NOT_CURRENT_POP_PLAYLIST=$(echo $NOT_CURRENT_POP_PLAYLIST_YOUTUBE)
NOT_CURRENT_POP_DIR_PATH="/main-disk/Goodies/Music/Not Current Pop/"

# 'kpop'
KPOP_PLAYLIST=$(echo $KPOP_PLAYLIST_YOUTUBE)
KPOP_DIR_PATH="/main-disk/Goodies/Music/kpop/"

DOWNLOAD_ARCHIVE_PATH="/main-disk/Goodies/Music/.playlists-downloaded.txt"

# UNCOMMENT FOR TESTING

# THE_PLAYLIST_DIR_PATH="/home/mathicc/test/second-final-test/"
# NOT_CURRENT_POP_DIR_PATH="/test/Not Current Pop/"
# KPOP_DIR_PATH="/test/kpop/"
# DOWNLOAD_ARCHIVE_PATH="/home/mathicc/test/second-final-test/.playlists-downloaded.txt"

# --

# Downloading
yt-dlp --extract-audio --audio-quality 0 --audio-format "mp3" --ignore-errors --add-metadata --download-archive "$DOWNLOAD_ARCHIVE_PATH" --no-post-overwrites --embed-thumbnail --output "$THE_PLAYLIST_DIR_PATH""+%(title)s %(id)s.%(ext)s" "$THE_PLAYLIST_PLAYLIST"
yt-dlp --extract-audio --audio-quality 0 --audio-format "mp3" --ignore-errors --add-metadata --download-archive "$DOWNLOAD_ARCHIVE_PATH" --no-post-overwrites --embed-thumbnail --output "$NOT_CURRENT_POP_DIR_PATH""+%(title)s %(id)s.%(ext)s" "$NOT_CURRENT_POP_PLAYLIST"
yt-dlp --extract-audio --audio-quality 0 --audio-format "mp3" --ignore-errors --add-metadata --download-archive "$DOWNLOAD_ARCHIVE_PATH" --no-post-overwrites --embed-thumbnail --output "$KPOP_DIR_PATH""+%(title)s %(id)s.%(ext)s" "$KPOP_PLAYLIST"

# Fixing album art
fix-album-art.py "$THE_PLAYLIST_DIR_PATH"
fix-album-art.py "$NOT_CURRENT_POP_DIR_PATH"
fix-album-art.py "$KPOP_DIR_PATH"
