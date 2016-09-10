#!/bin/bash

# it should be rot13

CHARS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  SUB="_LIH__A__T__MR__O_E_SFD_Y_"

echo " "
cat /krypton/krypton3/found3 | tr  "$CHARS" "$SUB"
echo " "
cat /krypton/krypton3/found3

