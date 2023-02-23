'''
The code in this sfotware is for maintaing the inventory record management. See the details of each funcaton.

'''

def ItemNameID(value, isName):
    #This funcation prints the value passed as an argument(parameter) based on
    # on the value of IsName
    if isName:
        print("Item Name: ", value)
    else:
        print("Item ID: ",value)


def printDetails(value):
    #This prints the value passed as an argument.
    print("Value :", value)
    


def CharsofValue():
    #This function calculates the size (i.e. number of characters) in 
    #item name and ID and store the size in global variables.
    global name_size 
    name_size = len(item_name)
    global ID_size
    ID_size = len(item_ID)



def ItemNameChar():
    #This function prints the item  name charachter by character.
    for ch in item_name:
        print(ch, end=' ')
    print()

def ItemIDChar():
    #This funcation claculates the item  ID charachter by character.
    for num in item_ID:
        print(num, end=' ')
    print()


def InputRecord():
    #This function takes input from user and store the item name and ID
    #in global variables. Call the other funcations for the printing and
    #size calculationa and printing character by character.
    global item_name
    global item_ID

    # taking input for student name and ID
    item_name = input("Enter item name: ")
    item_ID = input("Enter item ID: ")

    
if __name__ == "__main__":
    
    InputRecord()

    CharsofValue()

    ItemNameID(item_name, True)
    ItemNameID(item_ID, False)

    printDetails(name_size)
    printDetails(ID_size)

    ItemNameChar()
    ItemIDChar()
