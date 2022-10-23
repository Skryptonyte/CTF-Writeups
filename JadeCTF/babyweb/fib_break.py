

s1 = 1
s2 = 1

import requests
flag = ''
for i in range(200):
    
    c = requests.get("http://34.76.206.46:10008/?page={}".format(s2)).text
    print(c)
    temp = s1 + s2
    s1 = s2
    s2 = temp

    flag += c 

print(flag)