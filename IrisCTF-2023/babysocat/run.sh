#!/bin/bash
echo -n "Give me your command: "
read -e -r input
input="exec:./chal ls $input"

echo $input
FLAG="fakeflg{REDACTED}" socat - "$input" 
