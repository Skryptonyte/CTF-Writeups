from pwn import *
import binascii
r = remote('bob-alice-hard.hack.fe-ctf.dk',1337)
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

    for i in range(4):
        newr.append((r[16] & 0xf))
        newr.append((1 << 4) | ((r[16] & 0xf0) >> 4))
    send(cio,newr)


"""
)
bob = binascii.hexlify(b"""
while (1):
    r = recv(cio)[0]

    r.sort()
    newr = []

    f = {}
    arr = r[0:7]

    for j in arr:
        if j&0xf not in f:
            f[j&0xf] = 1
        else:
            f[j&0xf] += 1

    hb = 0
    lb = 0
    LB = 0
    for j in f.keys():
        if (f[j] == 7):
            hb = j
            lb = j
            LB = j
        elif (f[j] == 6):
            LB = j
            lb = j
        elif (f[j] == 5):
            LB = j
            hb = j
        elif ( f[j] == 4):
            LB = j
        elif (f[j] == 3):
            lb = j
            hb = j
        elif (f[j] == 2):
            lb = j
        elif f[j] == 1:
            hb = j
    newr.append((hb << 4) | lb)

    f = {}
    arr = r[7:14]

    for j in arr:
        if j & 0xf not in f:
            f[j & 0xf] = 1
        else:
            f[j & 0xf] += 1

    hb = 0
    lb = 0
    HB = 0
    for j in f.keys():
        if (f[j] == 7):
            hb = j
            lb = j
            HB = j
        elif (f[j] == 6):
            HB = j
            lb = j
        elif (f[j] == 5):
            HB = j
            hb = j
        elif ( f[j] == 4):
            HB = j
        elif (f[j] == 3):
            lb = j
            hb = j
        elif (f[j] == 2):
            lb = j
        elif f[j] == 1:
            hb = j
    newr.append((hb << 4) | lb)
    lastbyte = (HB << 4) | LB
    for i in range(14,56,3):
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
    newr.append(lastbyte)
    send(cio,newr)
""")

print(alice)
print(bob)
r.sendline(alice)
r.sendline(bob)

r.interactive()