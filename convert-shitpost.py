#!/usr/bin/python3

# Convert all videos that are not previewable
# by Discord to mp4

import os
import sys

dir_path = sys.argv[1]
sus_filetypes = ('mkv', 'webm')

for file in os.listdir(dir_path):
    file_ext = file.split('.')[-1]
    if file_ext in sus_filetypes:
        old_file = os.path.join(dir_path, file)
        new_file_name = file.replace(file_ext, 'mp4')
        os.system('ffmpeg -i \'{0}\' \'{1}\''
                  .format(old_file, os.path.join(dir_path, new_file_name)))
        os.remove(old_file)
