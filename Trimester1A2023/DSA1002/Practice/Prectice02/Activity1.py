import time

def factorial(x):#Max: 1558; Used 0 second
    result = 1
    while x > 1:
        result *= x
        x -= 1
    return result

def recursiveFactorial(x):#Max: 996; Used 0 second
    if x == 0:
        return 1
    else:
        return x * recursiveFactorial(x - 1)
    
def fibonacci(x):#Max: 20577; Used 0 second
    first = 0
    second = 1
    result = 1
    for i in range(x - 2):
        first = second
        second = result
        result = first + second
    return result
    
def recursiveFibonacci(x):# Needs more than 30s in 42 round
    if x == 0:
        return 0
    elif x == 1:
        return 1
    # elif x == 2:
    #     return 1
    else:
        return recursiveFibonacci(x - 1) + recursiveFibonacci(x - 2) 

def unitest(x):
    start_time = time.time()

    # print(f"Factorial function:\n{factorial(x)}")
    # print(f"Used {round(time.time() - start_time, 2)} second")
    # start_time = time.time()

    # print(f"Recursive Factorial function:\n{recursiveFactorial(x)}")
    # print(f"Used {round(time.time() - start_time, 2)} second")
    # start_time = time.time()

    # print(f"Fibonacci function:\n{fibonacci(x)}")
    # print(f"Used {round(time.time() - start_time, 2)} second")
    # start_time = time.time()

    print(f"Recursive Fibonacci function:\n{recursiveFibonacci(x)}")
    print(f"Used {round(time.time() - start_time, 2)} second")
    start_time = time.time()

def test(x):
    for i in range(x):
        print(f"\nRound {i}:\n")
        unitest(i)

if __name__ == "__main__":
    test(1000000)