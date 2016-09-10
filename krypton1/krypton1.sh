#!/bin/bash

CHARS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in `seq 0 ${#CHARS}`; do
    cat krypton2 | tr "[A-Z]" ${CHARS:$i}${CHARS:0:$i}
    #echo "HI $i"  
done
