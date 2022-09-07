#rock paper scissor--mini project

import random
user=0
computer=0
while True:
    a=int(input('''----SELECT YOUR CHOICE---
    1.ROCK
    2.PAPER
    3.SCISSOR
    4.EXIT\n'''))
    if a==4:
        print("thank you")
        break
    
    list1=[1,2,3]
    s=random.choice(list1)
    if s==1:
        print("computer choose ROCK")
    elif s==2:
        print("computer choose PAPER")
    elif s==3:
        print("computer choose SCISSOR")



    if a==s:
        print("tie")
    elif a==1:
        if s==2:
            print("computer win")
            computer=computer+1
        elif s==3:
            print("user win")
            user=user+1
    elif a==2:
        if s==1:
            print("user win")
            user=user+1
        elif s==3:
            print("computer win")
            computer=computer+1
    elif a==3:
        if s==1:
            print("computer win")
            computer=computer+1
        elif s==2:
            print("user win")
            user=user+1
            
print("user score",user)
print("computer score",computer)
    





