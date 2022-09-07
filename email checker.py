# valid email cheaker
import re

list1=["gmail.com","yahoo.com","hotmail.com","aol.com"]

eid=input("Enter your Email-id: ")
a=eid.split("@")
result1,result2=True,True
if len(a)==2:
    if len(a[0])<=64:
        p="^[A-z]+"
        d=re.search(p,a[0])
        if d:
            p="[!,#,$,%,&,',*,+,-,/,=,?,^,_,`,{,|]$"
            d=re.search(p,a[0])
            if d:
                result1=False
            else:
                p=a[0]
                v=["!","#","$","%","&","'","*","+","-","/","=","?","^","_","`","{","|"]
                c=0
                for i in p:
                    if i in v:
                        c+=1
                if c>1:
                    result1=False
                else:
                    result1=True                
        else:
            result1=False
    else:
        result1=False
        
    if a[1] in list1:
        result2=True
    else:
        result2=False

    if result1==True and result2==True:
        print("Valid")
    else:
        print("Invalid")
else:
    print("Invalid")













    

    


