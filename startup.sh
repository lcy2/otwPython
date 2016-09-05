#!/bin/bash



if [ -f $HOME/.vimrc ]
then
    echo ".vimrc file already exists."
else
    echo "syntax on" >> $HOME/.vimrc
    echo ".vimrc file created."
fi
    
