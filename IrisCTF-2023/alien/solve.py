from pwn import *


e = ELF("./alien_math")
table = e.read(e.address+0x2008,0x20a9-0x2008)
alienvals = table.split(b'\x00')
print(alienvals)


def convert_octal_to_alien(s):
    conv = b''
    for i in s:
        conv += alienvals[int(i)]  
    return conv


operations = \
[
    e.read(e.address+0x20db,0x20ef-0x20db+1),
    e.read(e.address+0x2103,0x2129-0x2103+1),
    e.read(e.address+0x213b,0x215b-0x213b+1),
    e.read(e.address+0x2167,0x2178-0x2167+1),
    e.read(e.address+0x2184,0x2195-0x2184+1),
    e.read(e.address+0x21a3,0x21bd-0x21a3+1),
]

funcs = \
[   lambda rand1, rand2: rand1 - rand2,
    lambda rand1, rand2: rand1^rand2,
    lambda rand1, rand2: 3 * rand2 // rand1,
    lambda rand1, rand2: 3 * rand1 % (rand2 * 3),
    lambda rand1, rand2: (rand1*rand1 + rand2),
    lambda rand1, rand2: 2 * (rand1 - rand2)
]

print(operations)
#p = process("./alien_math")

p = remote("alien.chal.irisc.tf",10600)
print(p.recv())
p.send(input("Proof of work:"))
p.recvline()

p.recvline()
p.recvline()
p.recvline()
p.recvline()


for i in range(0,68):
    problem = p.recvline()
    print("Processing Raw statement:",problem)
    problem = problem.replace(b"\xe3\x80\x82 \xe2\x94\xb4\xe2\x94\x98\xe2\x95\x9f\xe2\x94\x82 ",b",")
    problem = problem.replace(b"\xef\xbc\x9f\n",b"")

    for j in range(9):
        problem = problem.replace(alienvals[j],str(j).encode('utf-8'))
    operation = -1
    for j in range(6):
        if operations[j] in problem:
            operation = j
            problem = problem.replace(b' '+operations[j] + b' ',b',')
            break
    if (operation == -1):
        print("Invalid operation!")
        break
    print(problem)

    vals = problem.split(b',')
    problemno = int(vals[0][::-1],8)
    rand1 = int(vals[1][::-1],8)
    rand2 = int(vals[2][::-1],8)
    print("== Problem number:",problemno)
    print("Performing operation:",operation)

    print("Rand1:",rand1,"Rand2:",rand2)

    ans = funcs[operation](rand1,rand2)
    octans = oct(ans)[::-1].replace('o0','').replace('-','8')
    print("Solution:",ans)
    print("Solution in reverse octal:",octans)

    finalans = convert_octal_to_alien(octans)
    print("Alienified answer:",finalans)

    p.sendline(finalans)
    

p.interactive()