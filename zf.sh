#!/usr/bin/env zsh

# Open a folder with file explorer with the help of Zoxide

# REQUIREMENTS: zsh, zoxide installed (best if installed with oh-my-zsh)

eval "$(zoxide init zsh)"
z "$1" && f.sh
