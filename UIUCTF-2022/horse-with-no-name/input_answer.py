import random
# NOTE: random is imported only to replicate challenge conditions

#Actual answer: 
#index of flag.txt is 16, but if testing locally it may vary
(lambda:open(random._os.getcwd().__getitem__(0).__add__(random._os.listdir(random._os.getcwd().__getitem__(0)).__getitem__(16))))()
