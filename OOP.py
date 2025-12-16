class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("У вас недостатньо коштів")


# тест
x = BankAccount("Sasha", 500)
print(x.owner, x.balance)

x.deposit(400)
print(x.balance)

x.withdraw(300)
print(x.balance)
 



