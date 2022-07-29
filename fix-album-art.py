#!/bin/python3

# Script for fixing album art when downloading music from YouTube.
# Script removes left & right colored padding, thus making album art image squared.

import os
import sys
from PIL import Image

DIR_PATH = sys.argv[1]

for file_name in os.listdir(DIR_PATH):
    if file_name.startswith('+') and file_name.endswith('.mp3'):
        file_name = file_name.replace('$', '\\$')

        # Extract the image from mp3 file
        os.system(
            'ffmpeg -i "'
            + os.path.join(DIR_PATH, file_name)
            + '" -an -c:v copy "'
            + os.path.join(DIR_PATH, 'tmp-art-uncropped.jpg"')
        )

        # Crop & save the image
        im = Image.open(os.path.join(DIR_PATH, 'tmp-art-uncropped.jpg'))
        width, height = im.size

        left = int((width - height) / 2)
        upper = 0
        right = left + height
        lower = height

        im = im.crop((left, upper, right, lower))
        im.save(os.path.join(DIR_PATH, 'tmp-art-cropped.jpg'))

        # Embed the image
        os.system(
            'ffmpeg -i "'
            + os.path.join(DIR_PATH, file_name)
            + '" -i "'
            + os.path.join(DIR_PATH, 'tmp-art-cropped.jpg')
            + '" -map 0:0 -map 1:0 -c copy -id3v2_version 3 '
            + '-metadata:s:v title="Album cover" -metadata:s:v '
            + 'comment="Cover (front)" "'
            + os.path.join(DIR_PATH, file_name[1:])
            + '"'
        )

        # Clean up
        os.remove(os.path.join(DIR_PATH, 'tmp-art-uncropped.jpg'))
        os.remove(os.path.join(DIR_PATH, 'tmp-art-cropped.jpg'))
        file_name = file_name.replace('\\$', '$')
        os.remove(os.path.join(DIR_PATH, file_name))


print(f'\'{DIR_PATH.split("/")[-2]}\' done.')
