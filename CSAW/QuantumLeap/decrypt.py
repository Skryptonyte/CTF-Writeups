f = open("output").read()

flag = ""
for c in f:
    newbin = ""
    old = bin(ord(c))[2:]
    old = '0'*(8-len(old)) + old

    l = [old[0:2],old[2:4],old[4:6],old[6:8]]
    print(old)
    for i in l:
        if i == "10":
            newbin += "11"
        elif i == "11":
            newbin += "10"
        else:
            newbin += i

    flag += chr(int(newbin,2))

print(flag)