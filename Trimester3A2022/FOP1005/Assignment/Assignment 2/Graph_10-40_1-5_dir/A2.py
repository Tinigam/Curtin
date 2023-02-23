import random
import matplotlib.pyplot as plt
import numpy as np
import sys
from characters import *

XMAX = 200
YMAX = 200

num_vampires = 10
num_humans = 100
num_timesteps = 50
num_water = 10
num_food = 10
num_garlic = 10

if len(sys.argv) > 1:
    num_humans = int(sys.argv[1])

if len(sys.argv) > 2:
    num_vampires = int(sys.argv[2])

if len(sys.argv) > 3:
    num_timesteps = int(sys.argv[3])

# def interact(charList, objList):
#     for char1 in charList:
#         for char2 in charList[1:]:
#             if char1 != char2 and abs(char1.pos[0] - char2.pos[0]) < 8 and abs(char1.pos[1] - char2.pos[1]) < 8:
#                 char1.interaction(char2)
#                 print(f"{char1}interacted with{char2}")
#     for char in charList:
#         for obj in objList:
#             if char1 != char2 and abs(char.pos[0] - obj.pos[0]) < 8 and abs(char.pos[1] - obj.pos[1]) < 8:
#                 obj.interaction(char)

def interact(charList, objList):
    queue = charList.copy()
    visited = set()

    while queue:
        char1 = queue.pop(0)
        visited.add(char1)
        
        for char2 in charList:
            if char1 != char2 and char2 not in visited and abs(char1.pos[0] - char2.pos[0]) < 8 and abs(char1.pos[1] - char2.pos[1]) < 8:
                char1.interaction(char2)
                # print(f"{char1} interacted with {char2}")
                # queue.append(char2)
                visited.add(char2)
                
        for obj in objList:
            if char1 != obj and abs(char1.pos[0] - obj.pos[0]) < 8 and abs(char1.pos[1] - obj.pos[1]) < 8:
                obj.interaction(char1)
                # print(f"{obj} interacted with {char1}")

def main():
    characterList = []
    objectList = []
    for i in range(num_vampires):
        randX = random.randint(0, XMAX)
        randY = random.randint(0, YMAX)
        characterList.append(Character([randX, randY], [XMAX, YMAX], "Vampire"))

    for i in range(num_humans):
        randX = random.randint(0, XMAX)
        randY = random.randint(0, YMAX)
        characterList.append(Character([randX, randY], [XMAX, YMAX], "Human"))
    
    for i in range(num_water):
        randX = random.randint(0, XMAX)
        randY = random.randint(0, YMAX)
        objectList.append(Item([randX, randY], "Water"))

    for i in range(num_food):
        randX = random.randint(0, XMAX)
        randY = random.randint(0, YMAX)
        objectList.append(Item([randX, randY], "Food"))

    for i in range(num_garlic):
        randX = random.randint(0, XMAX)
        randY = random.randint(0, YMAX)
        objectList.append(Item([randX, randY], "Garlic"))
                
    for i in range(num_timesteps):
        # print("\n ### TIMESTEP ",i, "###")
        interact(characterList,objectList)
        for character in characterList:
            if character.health <= 0:
                characterList.remove(character)

        xvalues = []
        yvalues = []
        sizes = []
        colors = []
        for character in characterList:
            character.move()
            #print(character)
            xvalues.append(character.pos[0])
            yvalues.append(character.pos[1])
            sizes.append(character.getSize())
            colors.append(character.getColor())

        sxvalues = []
        syvalues = []
        ssizes = []
        scolors = []
        txvalues = []
        tyvalues = []
        tsizes = []
        tcolors = []
        for object in objectList:
            if object.state == "Water" or object.state == "Food":
                sxvalues.append(object.pos[0])
                syvalues.append(object.pos[1])
                ssizes.append(object.getSize())
                scolors.append(object.getColor())
            elif object.state == "Garlic":
                txvalues.append(object.pos[0])
                tyvalues.append(object.pos[1])
                tsizes.append(object.getSize())
                tcolors.append(object.getColor())
            else:
                SystemError

        plt.scatter(xvalues, yvalues, s = sizes, c = colors, marker = "o")   # Note plt origin is bottom left 
        plt.scatter(sxvalues, syvalues, s = ssizes, c = scolors, marker = "s")
        plt.scatter(txvalues, tyvalues, s = tsizes, c = tcolors, marker = "^")
        plt.xlim(0,XMAX)
        plt.ylim(0,YMAX)
        plt.pause(0.01)
        if i == num_timesteps - 1:
            plt.savefig(f"Population_H{num_humans}_V{num_vampires}.png")
        plt.clf()

    final_human = 0
    final_vampire = 0
    for character in characterList:
        if character.state == "Human":
            final_human += 1
        elif character.state == "Vampire":
            final_vampire += 1
        else:
            SystemError
    print(f"{num_humans},{final_human},{num_vampires},{final_vampire}")
    
if __name__ == "__main__":
    main()