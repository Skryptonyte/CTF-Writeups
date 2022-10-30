from pwn import *
import binascii
r = remote('bob-alice-easy.hack.fe-ctf.dk',1337)
#r = process('chal.py')

context.arch = 'amd64'

pi = 3
co = 4
ci = 5
po = 6



alice = binascii.hexlify(b"""
while (1):
    r = recv(cio)[0]

    newr = []
    for i in range(16):
        newr.append((i << 4) | (r[i] & 0xf))
        newr.append( (i << 4) | (r[i] & 0xf))
        newr.append( (i << 4) | ((r[i] & 0xf0) >> 4))
    send(cio,newr)


"""
)
bob = binascii.hexlify(b"""
while (1):
    r = recv(cio)[0]

    r.sort()
    newr = []
    for i in range(0,48,3):
        a = [r[i]&0xf,r[i+1]&0xf,r[i+2]&0xf]
        hb = 0 
        lb = 0
        for i in a:
            if (a.count(i) == 2):
                lb = i
            if (a.count(i) == 1):
                hb = i
            if (a.count(i) == 3):
                hb = i
                lb = i
                break
        newr.append((hb << 4) | lb)
    send(cio,newr)
""")

print(alice)
print(bob)
r.sendline(alice)
r.sendline(bob)

r.interactive()