#
# bingocard.py - generate a bingo card
#

import random

card = []

for i in range(18):
    card.append([])
    for j in range(9):
        card[i].append("")

for i in range(1, 90):
    x = int(i / 10)
    y = random.randint(0, 17)
    while card[y][x] != "":
        y = random.randint(0, 17)
    card[y][x] = i

for i in range(18):
    print(card[i], "\n")