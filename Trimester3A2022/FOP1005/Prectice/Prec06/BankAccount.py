class BankAccount():
    interest_rate = 0.03
    
    myclass = "BankAccount"
    def __init__ (self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def add_interest(self, amount):
        interest = self.balance * BankAccount.interest_rate
        self.balance = self.balance + interest