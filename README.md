## `extracc.py` - simple video downloading and clipping tool

```commandline
usage: extracc.py [-h] -u url -c clips [-d directory] [-q quality] [-e extension]

Make separate clips from a compilation video

options:
  -h, --help            show this help message and exit
  -u url, --url url     Video URL
  -c clips, --clips clips
                        Comma separated timestamps, no spaces. A clip is represented by a pair of respective timestamps so # of timestamps MUST BE EVEN
  -d directory, --directory directory
                        Destination directory
  -q quality, --quality quality
                        Video quality of extracted clips
  -e extension, --extension extension
                        File extension of generated clips

Example: python3 extracc.py -u https://www.youtube.com/watch?v=dQw4w9WgXcQ -c 0:0,0:12,0:15,0:20,1:0,2:1 -d /test/ -q shitpost -e mp4
```

### Requirements
Installed and added to PATH:
- yt-dlp
- ffmpeg

Additional Python libs:
- progress
___

## `f.sh` - open files or folders from command line with default apps. Works with native Linux and WSL.
___

## `shitpost.py` - download memes (video) more efficiently
___

## `apod.py` - NASA Astronomy Picture of the Day wallpaper setter
___

## `discordify.sh` - compress videos to just below 8MB