.global _start

_start:
.intel_syntax noprefix

mov r15, rsi
syscall
jmp r15
