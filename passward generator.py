#MINI PROJECT---(Random Passward Generator)


import string
import random

n=int(input("Enter digits of passward: "))

up=string.ascii_uppercase
rup=random.choice(up)

lo=string.ascii_lowercase
rlo=random.choice(lo)

dig=string.digits
rdig=random.choice(dig)

pun="@#$%&"
rpun=random.choice(pun)

passward=rup+rlo+rdig+rpun  
mix=up+lo+dig+pun

for i in range(n-4):
    a=random.choice(mix)
    passward=passward+a

b=list(passward)
random.shuffle(b)

passward=""
for i in b:
    passward=passward+i

print("random passward:",passward)    
    
