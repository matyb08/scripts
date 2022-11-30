#!/usr/bin/python3

import argparse
import shutil
import sys
import tempfile
import os
import subprocess as sp
import progress.bar as pg

parser = argparse.ArgumentParser(
    description='Make separate clips from a compilation video',
    epilog='Example: python3 extracc.py -u https://www.youtube.com/watch?v=dQw4w9WgXcQ -c 0:0,0:12,0:15,0:20,1:0,2:1 -d /test/ -q shitpost -e mp4'
)

parser.add_argument(
    '-u', '--url',
    dest='url', metavar='url',
    required=True, action='store',
    help='Video URL'
)
parser.add_argument(
    '-c', '--clips',
    dest='clips', metavar='clips',
    required=True, action='store',
    help='Comma separated timestamps, no spaces. A clip is represented by a pair of respective timestamps so # of timestamps MUST BE EVEN'
)
parser.add_argument(
    '-d', '--directory',
    dest='directory', metavar='directory',
    required=False, action='store', default='',
    help='Destination directory'
)
parser.add_argument(
    '-q', '--quality',
    dest='quality', metavar='quality',
    required=False, action='store', choices=('normal', 'shitpost'), default='normal',
    help='Video quality of extracted clips'
)
parser.add_argument(
    '-e', '--extension',
    dest='extension', metavar='extension',
    required=False, action='store',
    help='File format extension of generated clips'
)

args = parser.parse_args()

# Parse timestamps
timestamps = args.clips.split(',')
if len(timestamps) % 2 != 0:
    sys.stderr.write('Number of timestamps not even. Exiting...')
    exit(1)

clips = []
for i in range(0, len(timestamps), 2):
    clips.append((timestamps[i], timestamps[i + 1]))

# Check for duplicates in timestamps
if len(clips) != len(set(clips)):
    sys.stderr.write(f'Duplicate timestamps detected. Exiting...')
    exit(1)

# Check for yt-dlp and ffmpeg
if not shutil.which('yt-dlp'):
    sys.stderr.write(f'yt-dlp not installed or added to PATH. Exiting...')
    exit(1)

if not shutil.which('ffmpeg'):
    sys.stderr.write(f'yt-dlp not installed or added to PATH. Exiting...')
    exit(1)

# Check if directory exists
if args.directory != '':
    if not os.path.exists(args.directory):
        sys.stderr.write('Given directory doesn\'t exist. Exiting...')
        exit(1)

# Quality
if args.quality == 'normal':
    quality = []
else:
    quality = ['-f', 'mp4[height=720]+m4a/bestvideo[height<=720]+bestaudio']

# Download whole video
whole_video_name = sp.check_output([
    'yt-dlp',
    args.url,
    '--get-filename',
    '-o',
    '%(id)s.%(ext)s',
], ).decode('utf-8')[:-1]

whole_video_path = os.path.join(tempfile.gettempdir(), whole_video_name)
print('Downloading whole video...')
command_download = sp.run([
    'yt-dlp',
    args.url,
    '-o',
    whole_video_path,
    '--no-warnings',
    '--ignore-config',
    '--no-playlist'
] + quality)

if command_download.returncode != 0:
    sys.stderr.write('Error with downloading whole video. Exiting...')
    exit(command_download.returncode)

video_id = whole_video_name.split('.')[0]
extension = 'mp4' if not args.extension else args.extension

bar = pg.Bar('Clipping', max=len(clips), suffix='%(index)d/%(max)d clips')
bar.start()
for clip in clips:
    clip_path = os.path.join(args.directory, f'{video_id} {clip[0].replace(":", ".")}-{clip[1].replace(":", ".")}.{extension}')
    if not os.path.exists(clip_path):
        command_clip = sp.run([
            'ffmpeg',
            '-ss',
            clip[0],
            '-to',
            clip[1],
            '-i',
            whole_video_path,
            clip_path
        ], stderr=sp.DEVNULL, stdout=sp.DEVNULL)

        if command_clip.returncode != 0:
            sys.stderr.write('Error with clipping. Exiting...')
            os.remove(whole_video_path)
            exit(command_clip.returncode)

    bar.next()

# Clean up
os.remove(whole_video_path)

bar.finish()
