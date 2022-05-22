#!/bin/bash

# Open file browser more easily

if [ $# -eq 0 ]; then # '$#' gives the number of input arguments the script was passed
	dolphin > /dev/null 2>&1 &
	exit 0
fi

string=""

for piece in $@; do # $@ are all the args
	string+=$piece" "
done

string=${string::-1} # Remove last character
dolphin "$string" > /dev/null 2>&1 &
