f = open("./polyglot","rb")

from pwn import *

context.arch = 'amd64'
s = f.read()

p = run_shellcode(b'\x90'*15+s)  # Pad 15 bytes to make SSE instructions work

print(p.recv())
p.close()


context.arch = 'aarch64'

p = run_shellcode(s)

p.interactive()