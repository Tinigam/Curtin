#
# cointoss.py - simulate tossing a coin multiple times
#

import random

trials = input("Enter the number of tosses...\n")
coin = ['heads','tails']
heads = 0
tails = 0
trials = int(trials)

print('\nCOIN TOSS\n')

for index in range(trials):
    if random.choice(coin) == 'heads':
        heads = heads + 1
    else:
        tails = tails + 1

print('\nThere were ', heads, ' heads & ', tails, ' tails.\n')