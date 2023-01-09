from pwn import *


# Exploit the fact that password_hash takes only the first 72 chars

p = remote("stretchy.chal.irisc.tf",10704)


print(p.recv())
inp = input("Enter POW")
p.send(inp)

for i in range(16):
    for j in range(16):
        I = hex(i)[2:]
        J = hex(j)[2:]
        print(I,J)
        password = I*64 + J*8
        p.sendline(password)



print(p.recvuntil(b'}'))