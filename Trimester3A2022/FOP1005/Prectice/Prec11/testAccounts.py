from accounts import BankAccount

def balances():
    print('\n#### Balances ####\n')
    total = 0
    for i in range(len(my_accounts)):
        print("Name: ", my_accounts[i].name, "\tNumber: ", my_accounts[i].number, \
              "\tBalance: ", my_accounts[i].balance)
        total = total + my_accounts[i].balance
    print("\t\t\t\t\tTotal: ", total)

print('\n#### Bank Accounts ####\n')
my_accounts = []
