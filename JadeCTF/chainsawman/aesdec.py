from pwn import *

f = open("file.fun","rb")

import base64
from Crypto.Cipher import AES
key = base64.b64decode(b"OoIsAwwF32cICQoLDA0ODe==")
IV = b'\x00\x01\x00\x03\x05\x03\x00\x01\x00\x00\x02\x00\x06\x07\x06\x00'


print(len(IV))

aes = AES.new(key, AES.MODE_CBC, IV)

enc = f.read()
print(len(enc))
print(aes.decrypt(enc))
