import sys
import zlib

def swap(s, a, b):
    arr = list(s)
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp
    return "".join(arr)

def xor(s, a, b):
    arr = list(s)
    arr[a] = chr(ord(arr[a]) ^ ord(arr[b]))
    return "".join(arr)

def righthandswap(s, a, b):
    arr = bytearray(s)
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp
    return bytes(arr)

def righthandxor(s, a, b):
    arr = bytearray(s)
    arr[b] ^= arr[a]
    return bytes(arr)

def scramble1(flag):
    pos = 36
    while True:
        if pos == 0:
            flag = xor(flag, 25, 41)
            pos = 29
        elif pos == 1:
            flag = swap(flag, 4, 21)
            pos = 31
        elif pos == 2:
            flag = xor(flag, 24, 41)
            pos = 41
        elif pos == 3:
            flag = xor(flag, 16, 24)
            pos = 37
        elif pos == 4:
            flag = xor(flag, 0, 43)
            pos = 32
        elif pos == 5:
            flag = xor(flag, 24, 2)
            pos = 16
        elif pos == 6:
            flag = swap(flag, 18, 29)
            pos = 38
        elif pos == 7:
            flag = xor(flag, 28, 43)
            pos = 39
        elif pos == 8:
            flag = xor(flag, 25, 26)
            pos = 12
        elif pos == 9:
            flag = swap(flag, 4, 43)
            pos = 10
        elif pos == 10:
            flag = swap(flag, 15, 42)
            pos = 26
        elif pos == 11:
            flag = xor(flag, 33, 13)
            pos = 14
        elif pos == 12:
            flag = xor(flag, 43, 2)
            pos = 24
        elif pos == 13:
            flag = swap(flag, 7, 32)
            pos = 33
        elif pos == 14:
            flag = xor(flag, 20, 38)
            pos = 27
        elif pos == 15:
            flag = xor(flag, 16, 29)
            pos = 28
        elif pos == 16:
            flag = swap(flag, 8, 15)
            pos = 0
        elif pos == 17:
            flag = swap(flag, 17, 9)
            pos = 21
        elif pos == 18:
            flag = swap(flag, 37, 32)
            pos = 22
        elif pos == 19:
            flag = xor(flag, 34, 13)
            pos = 3
        elif pos == 20:
            flag = swap(flag, 21, 17)
            pos = 7
        elif pos == 21:
            flag = xor(flag, 8, 38)
            pos = 2
        elif pos == 22:
            flag = swap(flag, 13, 25)
            pos = 30
        elif pos == 23:
            flag = xor(flag, 33, 37)
            pos = 17
        elif pos == 24:
            flag = xor(flag, 15, 22)
            pos = 6
        elif pos == 25:
            flag = swap(flag, 24, 15)
            pos = 43
        elif pos == 26:
            flag = xor(flag, 37, 26)
            pos = 11
        elif pos == 27:
            flag = swap(flag, 9, 0)
            pos = 25
        elif pos == 28:
            flag = xor(flag, 32, 0)
            pos = 42
        elif pos == 29:
            flag = xor(flag, 24, 26)
            pos = 47
        elif pos == 30:
            flag = swap(flag, 1, 2)
            pos = 9
        elif pos == 31:
            flag = xor(flag, 18, 27)
            pos = 15
        elif pos == 32:
            flag = swap(flag, 26, 28)
            pos = 49
        elif pos == 33:
            flag = xor(flag, 24, 16)
            pos = 1
        elif pos == 34:
            flag = xor(flag, 11, 39)
            pos = 46
        elif pos == 35:
            flag = xor(flag, 19, 22)
            pos = 50
        elif pos == 36:
            flag = swap(flag, 28, 27)
            pos = 5
        elif pos == 37:
            flag = swap(flag, 13, 15)
            pos = 44
        elif pos == 38:
            flag = xor(flag, 6, 29)
            pos = 23
        elif pos == 39:
            flag = swap(flag, 15, 37)
            pos = 40
        elif pos == 40:
            flag = swap(flag, 40, 23)
            pos = 4
        elif pos == 41:
            flag = swap(flag, 28, 0)
            pos = 18
        elif pos == 42:
            flag = xor(flag, 41, 19)
            pos = 19
        elif pos == 43:
            flag = swap(flag, 7, 5)
            pos = 20
        elif pos == 44:
            flag = xor(flag, 12, 40)
            pos = 35
        elif pos == 45:
            flag = swap(flag, 19, 30)
            pos = 48
        elif pos == 46:
            flag = swap(flag, 15, 4)
            pos = 13
        elif pos == 47:
            flag = swap(flag, 17, 11)
            pos = 45
        elif pos == 48:
            flag = xor(flag, 8, 28)
            pos = 8
        elif pos == 49:
            flag = xor(flag, 19, 9)
            pos = 34
        elif pos == 50:
            return

def scramble2(flag):
    pos = 48
    while True:
        if pos == 0:
            flag = righthandswap(flag, 13, 25)
            pos = 5
        elif pos == 1:
            flag = donut(flag, 16, 4)
            pos = 42
        elif pos == 2:
            flag = righthandswap(flag, 22, 4)
            pos = 41
        elif pos == 3:
            flag = donut(flag, 39, 47)
            pos = 44
        elif pos == 4:
            flag = righthandswap(flag, 29, 41)
            pos = 17
        elif pos == 5:
            flag = donut(flag, 18, 36)
            pos = 13
        elif pos == 6:
            flag = donut(flag, 25, 23)
            pos = 31
        elif pos == 7:
            flag = donut(flag, 37, 49)
            pos = 39
        elif pos == 8:
            flag = donut(flag, 23, 30)
            pos = 24
        elif pos == 9:
            flag = righthandswap(flag, 32, 11)
            pos = 38
        elif pos == 10:
            flag = donut(flag, 24, 14)
            pos = 3
        elif pos == 11:
            flag = donut(flag, 31, 23)
            pos = 26
        elif pos == 12:
            flag = donut(flag, 25, 9)
            pos = 36
        elif pos == 13:
            flag = righthandswap(flag, 37, 0)
            pos = 37
        elif pos == 14:
            flag = donut(flag, 30, 35)
            pos = 32
        elif pos == 15:
            flag = righthandswap(flag, 21, 2)
            pos = 27
        elif pos == 16:
            flag = righthandswap(flag, 23, 44)
            pos = 19
        elif pos == 17:
            flag = righthandswap(flag, 1, 51)
            pos = 29
        elif pos == 18:
            flag = righthandswap(flag, 21, 16)
            pos = 35
        elif pos == 19:
            flag = righthandswap(flag, 35, 33)
            pos = 34
        elif pos == 20:
            flag = righthandswap(flag, 18, 1)
            pos = 30
        elif pos == 21:
            flag = righthandswap(flag, 3, 27)
            pos = 45
        elif pos == 22:
            flag = donut(flag, 2, 13)
            pos = 18
        elif pos == 23:
            flag = donut(flag, 27, 50)
            pos = 10
        elif pos == 24:
            flag = righthandswap(flag, 27, 45)
            pos = 20
        elif pos == 25:
            flag = righthandswap(flag, 49, 35)
            pos = 6
        elif pos == 26:
            flag = righthandswap(flag, 13, 40)
            pos = 4
        elif pos == 27:
            flag = righthandswap(flag, 47, 50)
            pos = 8
        elif pos == 28:
            flag = donut(flag, 0, 1)
            pos = 43
        elif pos == 29:
            flag = donut(flag, 3, 34)
            pos = 49
        elif pos == 30:
            flag = donut(flag, 50, 7)
            pos = 11
        elif pos == 31:
            flag = donut(flag, 41, 9)
            pos = 23
        elif pos == 32:
            flag = donut(flag, 44, 50)
            pos = 16
        elif pos == 33:
            flag = righthandswap(flag, 19, 29)
            pos = 15
        elif pos == 34:
            flag = righthandswap(flag, 34, 47)
            pos = 40
        elif pos == 35:
            flag = righthandswap(flag, 24, 3)
            pos = 47
        elif pos == 36:
            flag = righthandswap(flag, 14, 37)
            pos = 0
        elif pos == 37:
            flag = donut(flag, 21, 29)
            pos = 25
        elif pos == 38:
            flag = donut(flag, 29, 1)
            pos = 1
        elif pos == 39:
            flag = righthandswap(flag, 23, 37)
            pos = 33
        elif pos == 40:
            flag = righthandswap(flag, 29, 44)
            pos = 12
        elif pos == 41:
            flag = donut(flag, 19, 39)
            pos = 50
        elif pos == 42:
            flag = righthandswap(flag, 8, 37)
            pos = 28
        elif pos == 43:
            flag = donut(flag, 40, 25)
            pos = 21
        elif pos == 44:
            flag = donut(flag, 46, 14)
            pos = 7
        elif pos == 45:
            flag = donut(flag, 36, 39)
            pos = 22
        elif pos == 46:
            flag = righthandswap(flag, 44, 6)
            pos = 9
        elif pos == 47:
            flag = righthandswap(flag, 46, 28)
            pos = 14
        elif pos == 48:
            flag = donut(flag, 16, 50)
            pos = 46
        elif pos == 49:
            flag = righthandswap(flag, 29, 10)
            pos = 2
        elif pos == 50:
            return

def main():
    if len(sys.argv) <= 1:
        print("Missing argument")
        exit(1)

    flag_to_check = sys.argv[1]

    flag_length = len(flag_to_check)
    if flag_length < 44:
        print("Incorrect")
        exit(1)

    scramble1(flag_to_check)

    flag_compressed = zlib.compress(flag_to_check.encode("utf-8"))

    flag_compressed_length = len(flag_compressed)
    if flag_compressed_length < 52:
        print("Incorrect")
        exit(1)

    scramble2(flag_compressed)

    if flag_compressed == b'x\x9c\xcb,\xca,N.I\xab.\xc9\xc8,\x8e7,\x8eOIM3\xcc3,1\xce\xa9\x8c7\x89/\xa8,\xc90\xc8\x8bO\xcc)2L\xcf(\xa9\x05\x00\x83\x0c\x10\xf9':
        print("Correct!")
    else:
        print("Incorrect!")


def decryptFlag():
    flag_compressed = b'x\x9c\xcb,\xca,N.I\xab.\xc9\xc8,\x8e7,\x8eOIM3\xcc3,1\xce\xa9\x8c7\x89/\xa8,\xc90\xc8\x8bO\xcc)2L\xcf(\xa9\x05\x00\x83\x0c\x10\xf9'

    flag_to_check = zlib.decompress(flag_compressed)

    print(flag_to_check)

decryptFlag()