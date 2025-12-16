class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if self.balance > amount:
            self.balance -= amount
        elif self.balance < amount:
            print("У вас недостатньо коштів")

    
x = BankAccount("Sasha",100)
print(x.owner, x.balance)
print(x.balance)
x.withdraw(300)
print(x.balance)
 



