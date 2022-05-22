#!/bin/python3

# Open websites from URLs in a browser

import os
import sys

command = 'brave-browser' # Browser command

if len(sys.argv) == 1:
    file_path = 'sites.txt'
else:
    file_path = sys.argv[1]

with open(file_path, 'r') as sites_file:
    for link in sites_file.read().split('\n'):
        command += f' \'{link}\''

os.system(f'{command}&')

