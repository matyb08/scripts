#!/bin/sh

# Mount an MTP device on linux

# https://www.howtoforge.com/tutorial/how-to-connect-your-android-device-on-linux/

if [ "$1" = "-u" ]; then
	sudo umount /mnt/phone/
	exit 0
fi

read -p "Connect the phone, hit ENTER: " enter
mtp-detect # Triggers phone to show wheather you allow access to phone data
read -p "Press ALLOW on phone to allow file access, hit ENTER: " enter
sudo umount /mnt/phone/ > /dev/null 2>&1
sudo pkill kiod5 > /dev/null 2>&1
sudo jmtpfs -o allow_other /mnt/phone/
