

flag = [0xa,3,0xd,0x1f,0x1f,0x18,7,9,0x27,2,0x19,1,0xf,0xc,0xd,3,1,0x33,0x16,5,1,0xa,0x1f,0x27, 5, 0x1e, 0xa, 0x33, 0x19, 0x38, 0xf, 0, 1, 0x15, 0x11, 0x18, 0xe, 0x18, 0x11, 0x12, 0x9, 0x30, 0x1c, 0xa, 0xb, 0x1c, 0xa, 0x1e,0xc, 0x1d, 0x33, 5, 3, 0x13, 1, 0x33,8,9,0xc, 0x3b, 5, 0x1b, 0x11]



bonus = [0x53, 0x50, 0x53, 0x47, 0x5b, 0x26, 0x25]
keyenc = [ord(x) for x in "flag{"]

key = ""
for i in range(len(keyenc)):
    key += chr(flag[i] ^ keyenc[i])



flagdec = ""
for i in range(len(flag)):
    flagdec += chr(flag[i] ^ ord(key[i % len(key)]))

print(flagdec)