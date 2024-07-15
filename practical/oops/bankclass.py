class Bank():
    print("welcome to bank class")
    print("enter values to get details")
    def __init__(self,name,branch,balance):
                self.bname=name
                self.bbranch=branch
                self.bbalance=balance
    def display(self):
        print("bank Name:", self.bname)
        print("bank branch:", self.bbranch)
        print("bank balance:", self.bbalance)


    def credits(self,new_balance):
                 if new_balance>100:
                    self.bbalance=self.bbalance+new_balance

                 else:
                    print("Insufficient Balance to add")

                 print("bank Name:", self.bname)
                 print("bank branch:", self.bbranch)
                 print("bank balance:", self.bbalance)


    def debits(self,amount):
                if self.bbalance>200:
                    self.bbalance=self.bbalance-amount

                else:
                  print("Insufficient Balance to deposit")
                print("bank Name:", self.bname)
                print("bank branch:", self.bbranch)
                print("bank balance:", self.bbalance)

v1 = Bank("SBI", "tirupathi", 20000)


while True:
    print('1.Display Details')
    print('2.Credit Amount')
    print('3.debit amount')
    print('exit loop')
    choice = int(input('ENter your choice'))
    if choice == 1:
        v1.display()
    elif choice == 2:
        Newamount = int(input('ENter your credit amount :'))
        v1.credits(Newamount)
    elif choice == 3:
        debitamount = int(input('Enter a debit amount:'))
        v1.debits(debitamount)
    else:
        print('You have given Invalid Input \n ------THANK YOU ---')
        break





