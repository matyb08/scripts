#!/usr/bin/env sh

# Open files or folders from command line with default apps.
# Works with native Linux and WSL.

# REQUIREMENTS: /

if [ $# -eq 0 ]; then # '$#' gives the number of input arguments the script was passed
	if grep -qi microsoft /proc/version; then
		powershell.exe -c start $(wslpath -aw .)
		exit 0
	else
		xdg-open . > /dev/null 2>&1 &
		exit 0
	fi

else
	if grep -qi microsoft /proc/version; then
		for path in $@; do
			powershell.exe -c start $(wslpath -aw $path)
		done
                exit 0
        else
		xdg-open $@ > /dev/null 2>&1 &
		exit 0
	fi
fi
