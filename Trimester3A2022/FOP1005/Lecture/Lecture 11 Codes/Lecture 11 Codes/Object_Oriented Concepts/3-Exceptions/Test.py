from BankAccount import *

acc1 = BankAccount(11111, 1000)

try:
	amount = float(input("Enter amount to withdraw:$"))
	acc1.withdraw(amount)
	print("Transaction done")
	print("Balance:")
	acc1.printit()
except MoneyNotEnoughException as moneyNotEnff:
	print("Money not enough")
	print(f"Lack of ${moneyNotEnff.amount}")

