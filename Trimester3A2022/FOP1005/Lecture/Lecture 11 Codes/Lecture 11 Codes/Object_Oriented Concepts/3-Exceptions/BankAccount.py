class BankAccount:

    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            raise MoneyNotEnoughException(amount - self.balance)

    def printit(self):
        print(self.acc_no)
        print(self.balance)


class MoneyNotEnoughException(Exception):

    def __init__(self, amount):
        self.amount = amount

