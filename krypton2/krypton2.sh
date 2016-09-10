#!/bin/bash

# it should be rot13

CHARS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in `seq 0 ${#CHARS}`; do
        echo -n "$i  " 
        cat /krypton/krypton2/krypton3  | tr "[A-Z]" ${CHARS:$i}${CHARS:0:$i} | tr '[:upper:]' '[:lower:]'
        echo " "
        #echo "HI $i"  
        done

