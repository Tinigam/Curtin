#
# dicetoss.py - simulate tossing a dice multiple times
#

import random

trials = input("Enter the number of tosses...\n")
dice = range(5)
num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0
num6 = 0

print('\nDICE TOSS\n')

for index in range(int(trials)):
    number = random.randint(1,6)
    if number == 1:
        num1 = num1 + 1
    elif number == 2:
        num2 = num2 + 1
    elif number == 3:
        num3 = num3 + 1
    elif number == 4:
        num4 = num4 + 1
    elif number == 5:
        num5 = num5 + 1
    else:
        num6 = num6 + 1
    

print('\nThere were\n', num1, ' 1s.\n', num2, ' 2s.\n', num3, ' 3s.\n', num4, ' 4s.\n', num5, ' 5s.\n', num6, ' 6s.\n')