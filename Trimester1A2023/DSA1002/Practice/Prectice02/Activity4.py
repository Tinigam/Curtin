def recursiveFactorial(x):
        if x == 0:
            return 1
        else:
            return x * recursiveFactorial(x - 1)
    
def recursiveFibonacci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return recursiveFibonacci(x - 1) + recursiveFibonacci(x - 2) 
    
def recursiveGcd(x, y):
    if y == 0:
        return abs(x)
    else:
        return recursiveGcd(y, x % y)

def DecConvertor(x, target):
    if x >= (target - 1):
        DecConvertor(x // target, target)
    print(x % target, end = "")

def factotialCal():
    inVal = input("Please enter a non-negative number:\n")
    try:
        inVal = int(inVal)
        print(f"The factorial of {inVal} is {recursiveFactorial(inVal)}")
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
        print(f"The {inVal}th fibonacci number is {recursiveFibonacci(inVal)}")
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
        print(f"The greatest common denominator of {inVal1} and {inVal2} is {recursiveGcd(inVal1, inVal2)}")
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
        DecConvertor(inVal, targetVal)
    except ValueError:
        print("Please try again!")
        decConvertCal()
    except RecursionError:
        print("Please try again!")
        decConvertCal()