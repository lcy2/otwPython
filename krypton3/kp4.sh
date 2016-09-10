#!/bin/bash



CHARS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"


TOTAL=$(egrep -o '[A-Z]' /krypton/krypton3/found* | wc -l)
echo $TOTAL


for i in `seq 0 $((${#CHARS}-1))`; do
    echo -n "${CHARS:$i:1} " 
    #cat /krypton/krypton3/found3  | tr "[A-Z]" ${CHARS:$i}${CHARS:0:$i} | tr '[:upper:]' '[:lower:]'
    echo $(($(egrep -o "${CHARS:$i:1}" /krypton/krypton3/found* | wc -l)))
    #echo " "
done



echo "-----------------"

for i in `seq 0 $((${#CHARS}-1))`; do
    for j in `seq 0 $((${#CHARS}-1))`; do
    echo -n "${CHARS:$i:1}${CHARS:$j:1} " 
    #cat /krypton/krypton3/found3  | tr "[A-Z]" ${CHARS:$i}${CHARS:0:$i} | tr '[:upper:]' '[:lower:]'
    echo $(($(egrep -o "${CHARS:$i:1}${CHARS:$j:1}" /krypton/krypton3/found* | wc -l)*10000/TOTAL))
    #echo " "
done
done

