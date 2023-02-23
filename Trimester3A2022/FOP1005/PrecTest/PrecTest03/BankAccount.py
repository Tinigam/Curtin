class BankAccount:
    BankFee = 5
    myclass = "BankAccount"
    def __init__(self, name, acc_no, balance):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount - BankAccount.BankFee

    def withdraw(self, amount):
        if self.balance - amount - BankAccount.BankFee >= 0:
            self.balance -= amount + BankAccount.BankFee
            return True
        else:
            return False

    def __str__(self):
        return f"Name: {self.name}, AccNo: {self.acc_no}, Balance: {self.balance}"