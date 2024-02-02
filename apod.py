#!/usr/bin/env python3

# NASA Astronomy Picture of the Day wallpaper setter

# REQUIREMENTS: pip install requests beautifulsoup4 lxml python-slugify

import requests
import subprocess
import os
import ctypes
import sys
from bs4 import BeautifulSoup
from slugify import slugify

os.chdir(sys.argv[1])
soup = BeautifulSoup(requests.get('https://apod.nasa.gov/apod/astropix.html').text, 'lxml')

try:
  image_url = 'https://apod.nasa.gov/apod/' + soup.select('body > center:nth-child(1) > p:nth-child(3) > a')[0]['href']
except IndexError: # not an image post
  exit(1)

description = soup.select('body > p:nth-child(3)')[0].text.replace('\n\n', ' ').replace('\n', ' ').replace('  ', ' ').strip() + '\n\n' + soup.select('body > center:nth-child(1) > p:nth-child(3)')[0].text.strip()
title = soup.select('body > center:nth-child(2) > b:nth-child(1)')[0].text.strip()
image_extension = image_url.split('/')[-1].split('.')[-1]
image_unique_name = image_url.split('/')[-1].split('.')[-2]
image_filename = f'{slugify(title)} ({image_unique_name}).{image_extension}'
description_filename = f'{slugify(title)} ({image_unique_name}).txt'

# duplication check
if os.path.isfile(image_filename):
  exit(0)

image_data = requests.get(image_url).content
with open(image_filename, 'wb') as f:
  f.write(image_data)

with open(description_filename, 'w') as f:
  f.write(description)

ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath(image_filename), 0) # set background
