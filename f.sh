#!/usr/bin/env bash

# Open files or folders from command line with default apps or (preferably) with Total Commander, in case of folders.
# Works with native Linux and WSL.

# REQUIREMENTS: total commander (added to PATH)

if [ $# -eq 0 ]; then # at least one path is given
    if grep -qi microsoft /proc/version; then
        if command -v totalcmd64.exe >/dev/null 2>&1; then
            powershell.exe -c "totalcmd64.exe /O /T /L=\"$(wslpath -aw ".")\""
        else
            powershell.exe -c "start '$(wslpath -aw ".")'"
        fi
        exit 0
    else
        xdg-open . > /dev/null 2>&1 &
        exit 0
    fi

else # no path is given
    if grep -qi microsoft /proc/version; then
        for path in "$@"; do
            if [ -d "$path" ] && command -v totalcmd64.exe >/dev/null 2>&1; then
                powershell.exe -c "totalcmd64.exe /O /T /L=\"$(wslpath -aw "$path")\""
            else
                powershell.exe -c "start '$(wslpath -aw "$path")'"
            fi
        done
        exit 0
    else
        xdg-open $@ > /dev/null 2>&1 &
        exit 0
    fi
fi