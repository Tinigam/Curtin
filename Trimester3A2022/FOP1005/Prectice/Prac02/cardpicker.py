#
# assorted.py - selecting random card from a pack
#

import random

card = []

card.extend(['Heart']*13)
card.extend(['Tile']*13)
card.extend(['Clover']*13)
card.extend(['Pike']*13)
card.extend(['Joker']*2)

print('\nASSORTED CREAMS\n')

print('There are ', len(card), ' cards in the pack.')

print('\n', card, '\n')

more = input('\nWould you like 5 cards (Y/N)... ')


while more != 'N':
    for num in range(5):
        choice = random.randint(0,len(card)-1)
        print('Your card is : ', card[choice])
        del card[choice]
    if len(card) <= 4:
        print("\nYou can\'t draw more cards!")
        break
    more = input('\nWould you like a card (Y/N)...')

print('\nThere are ', len(card), ' cards left.')
print('\n', card, '\n')