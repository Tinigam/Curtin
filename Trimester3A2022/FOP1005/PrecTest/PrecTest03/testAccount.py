from BankAccount import *

accounts = [
    BankAccount("John Doe", 12345, 1000),
    BankAccount("Jane Smith", 23456, 2000),
    BankAccount("Bob Johnson", 34567, 3000),
    BankAccount("Alice Williams", 45678, 4000),
    BankAccount("Michael Brown", 56789, 5000)
]

for account in accounts:
    print(account)

while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("Select an account:")
        for i, account in enumerate(accounts):
            print(f"{i+1}. {account.name}")
        acc_choice = int(input()) - 1

        amount = int(input("Enter an amount to deposit: "))
        accounts[acc_choice].deposit(amount)
        print(f"Bank fee: {BankAccount.BankFee}")
    elif choice == "2":
        print("Select an account:")
        for i, account in enumerate(accounts):
            print(f"{i+1}. {account.name}")
        acc_choice = int(input()) - 1

        amount = int(input("Enter an amount to withdraw: "))
        try:
            accounts[acc_choice].withdraw(amount)
            print(f"Bank fee: {BankAccount.BankFee}")
        except ValueError:
            print("You don't have that much money!")
    elif choice == "3":
        break
    else:
        print("Invalid choice.")