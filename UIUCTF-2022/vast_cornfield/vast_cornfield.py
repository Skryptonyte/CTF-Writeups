flag = list("odt_sjtfnb_jc_c_fiajb_he_ciuh_nkn_atvfjp")

alphabet = "abcdefghijklmnoprstuvwxyz"
corn_alphabet = "cornfieldsabghjkmptuvwxyz"
vast_alphabet = "vastbcdefghijklmnopruwxyz"

def next_valid_index(flag, i):
    
    while (i < len(flag) and flag[i] == '_'):
        i = i + 1
    return i


i = next_valid_index(flag,0)
j = next_valid_index(flag,i+1)

while (i < len(flag) and j < len(flag)):
    i1 = vast_alphabet.index(flag[i])
    i2 = corn_alphabet.index(flag[j])

    c1 = i1 // 5
    c2 = i1 % 5

    c3 = i2 // 5
    c4 = i2 % 5
    A
    flag[i] = alphabet[c1*5 + c4]
    flag[j] = alphabet[c3*5 + c2]

    i = next_valid_index(flag,j+1)
    j = next_valid_index(flag,i+1)

print(''.join(flag))






