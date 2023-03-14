import Activity1, Activity2, Activity3

def factotialCal():
    inVal = input("Please enter a non-negative number:\n")
    try:
        inVal = int(inVal)
        print(f"The factorial of {inVal} is {Activity1.recursiveFactorial(inVal)}")
    except ValueError:
        print(f"{inVal} is not a number! please try again!")
        factotialCal()
    except RecursionError:
        print(f"{inVal} should be a non-negative number! Please try again!")
        factotialCal()

def fibonacciCal():
    inVal = input("Please enter a non-negative number:\n")
    try:
        inVal = int(inVal)
        print(f"The {inVal}th fibonacci number is {Activity1.recursiveFibonacci(inVal)}")
    except ValueError:
        print(f"{inVal} is not a number! please try again!")
        fibonacciCal()
    except RecursionError:
        print(f"{inVal} should be a non-negative number! Please try again!")
        fibonacciCal()

def gcdCal():
    inVal1 = input("Please enter first number:\n")
    inVal2 = input("Please enter second number:\n")
    try:
        inVal1 = int(inVal1)
        inVal2 = int(inVal2)
        print(f"The greatest common denominator of {inVal1} and {inVal2} is {Activity2.recursiveGcd(inVal1, inVal2)}")
    except ValueError:
        print("Both numbers have to be valuses, Please try again!")
        gcdCal()
    except RecursionError:
        print("Please try again!")
        gcdCal()

def decConvertCal():
    inVal = input("Please enter the decimal number to convert:\n")
    targetVal = input("Please enter the base you want to convert to:\n")
    try:
        inVal = int(inVal)
        targetVal = int(targetVal)
        Activity3.DecConvertor(inVal, targetVal)
    except ValueError:
        print("Please try again!")
        decConvertCal()
    except RecursionError:
        print("Please try again!")
        decConvertCal()

def main():
    print("""Please enter the function to use:\n
    1. Factorial Calculator
    2. Fibonacci Calculator
    3. Greatest common denominator Calculator
    4. Decimal Transform Calculator\n""")
    inVal = input("Please enter here: ")
    if inVal == "1":
        factotialCal()
    elif inVal == "2":
        fibonacciCal()
    elif inVal == "3":
        gcdCal()
    elif inVal == "4":
        decConvertCal()
    else:
        raise ValueError("Input should be a number between 1 - 4, Please try again!")
    
main()