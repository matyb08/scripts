#!/usr/bin/env bash

# Open files or folders from command line with default apps or (preferably) with Total Commander, in case of folders.
# Works with native Linux and WSL.

# REQUIREMENTS: total commander (added to PATH)

# no path is given
if [ $# -eq 0 ]; then
    # wsl
    if grep -qi microsoft /proc/version; then
        if command -v totalcmd64.exe >/dev/null 2>&1; then
            powershell.exe -c "totalcmd64.exe /O /T /L=\"$(wslpath -aw ".")\""
        else
            powershell.exe -c "start '$(wslpath -aw ".")'"
        fi
  
    # native
    else
        xdg-open . > /dev/null 2>&1 &
    fi

# one or more paths are given
else
    # wsl
    if grep -qi microsoft /proc/version; then
        for path in "$@"; do
            if [ -d "$path" ] && command -v totalcmd64.exe >/dev/null 2>&1; then
                powershell.exe -c "totalcmd64.exe /O /T /L=\"$(wslpath -aw "$path")\""
            else
                powershell.exe -c "start '$(wslpath -aw "$path")'"
            fi
        done
  
    # native
    else
        for path in "$@"; do
            xdg-open "$path" > /dev/null 2>&1 &
        done
    fi
fi