class bank:
    def __init__(self,bal):
        self.balance=bal
    def withdraw(self):
        w_amt=float(input("Enter the withdrawal amt: "))
        if w_amt<self.balance:
            self.balance=self.balance-w_amt
            print("balance:",self.balance)
        else:
            print("insuficent balance")
    def deposit(self):
        d_amt=float(input("Enter the deposit amt: "))
        self.balance=self.balance+d_amt
        print("balance:",self.balance)
    def display(self):
        print("balance:",self.balance)
        
b=bank(10000)

while True:
    a=int(input('''----MENU----
1.to withdraw
2.to deposit
3.to check balance
4.exit\n'''))

    if a==1:
        b.withdraw()
    elif a==2:
        b.deposit()
    elif a==3:
        b.display()
    elif a==4:
        print("thank you")
        break
    else:
        print("invalid input")

