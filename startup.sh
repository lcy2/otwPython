#!/bin/bash

# Turn on syntax coloring in vi

echo -n "1. "
if [ -f $HOME/.vimrc ]
then
    echo ".vimrc file already exists."
else
    echo "syntax on" >> $HOME/.vimrc
    echo "set expandtab shiftwidth=4 softtabstop=0 autoindent tabstop=4" >> $HOME/.vimrc
    echo ".vimrc file created."
fi

# Edit local git config for syncing with Github
echo -n "2. "
git config --global user.name "lcy2"
git config --global user.email "lichangyi888@hotmail.com"
echo "git config set."
