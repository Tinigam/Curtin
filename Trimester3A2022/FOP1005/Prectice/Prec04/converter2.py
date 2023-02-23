#
# converter2.py - convert between temperature format.
#

def fahr2cel(fahr):
    """Convert from Fahrenheit to Celsius.
    Argument:
    fahr - the temperature in Fahrenheit
    """
    celsius = (fahr - 32) * (5/9)
    return celsius

def cel2fahr(cel):
    """Convert from Celsius to Fahrenheit.
    Argument:
    cel - the temperature in Celsius
    """
    fahrenheit = cel * (9/5) + 32
    return fahrenheit

def cel2kel(cel):
    """Convert from Celsius to Kelvin.
    Argument:
    cel - the temperature in Celsius
    """
    kelvin = cel + 273.15
    return kelvin

def kel2cel(kel):
    """Convert from Kelvin to Celsius.
    Argument:
    kel - the temperature in Kelvin
    """
    celsius = kel - 273.15
    return celsius

def fahr2kel(fahr):
    """Convert from Fahrenheit to Kelvin.
    Argument:
    fahr - the temperature in Fahrenheit
    """
    kelvin = (fahr + 459.67) * (5/9)
    return kelvin

def kel2fahr(kel):
    """Convert from Kelvin to Celsius.
    Argument:
    kel - the temperature in Kelvin
    """
    fahrenheit = kel * (9/5) - 459.67
    return fahrenheit


print("/nTEMPERATURE CONVERTOR/n")
finish = False

def printMenuAndGetAChoice():
    print("1. Fahrenheit")
    print("2. Celsius")
    print("3. Kelvin")
    choice = int(input("Enter the original value type: "))
    return choice

while finish == False:
    choice = printMenuAndGetAChoice()
    value = float(input("Enter a value of temperature"))
    if (choice == 1):
        print("Fahrenheit: ", value, "Celsius: ", fahr2cel(value), "Kelvin: ", fahr2kel(value))
    elif (choice == 2):
        print("Celsius: ", value, "Fahrenheit: ", cel2fahr(value), "Kelvin: ", cel2kel(value))
    elif (choice == 3):
        print("Kelvin: ", value, "Celsius: ", kel2cel(value), "Fahrenheit: ", kel2fahr(value))
    else:
        print("Invalid Choice")
    cont = input("Continue? (Y/N)")
    if cont == "N":
        finish = True
    