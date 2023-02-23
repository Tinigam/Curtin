import random
import math

class Character():

    def __init__(self, pos, mapSize, state):
        self.pos = pos
        self.state = state
        if state == "Human":
            self.step = 4
        else:
            self.step = 8

        self.health = 100
        self.age = random.randint(10, 51)
        self.mapSize = mapSize

    def __str__(self):
        return self.state + " @ " + str(self.pos)

    def move(self):
        angle = random.uniform(0, 360) * (math.pi / 180)
        dx = self.step * math.cos(angle)
        dy = self.step * math.sin(angle)
        self.pos[0] += dx
        self.pos[1] += dy

        if self.pos[0] < 0:
            self.pos[0] = 0
        elif self.pos[0] >= self.mapSize[0]:
            self.pos[0] = self.mapSize[0]
        
        if self.pos[1] < 0:
            self.pos[1] = 0
        elif self.pos[1] >= self.mapSize[1]:
            self.pos[1] = self.mapSize[1]

        if self.state == "Human":
            self.health -= 1
            self.age += 1
            if self.age > 70:
                self.health = 0
        elif self.state == "Vampire":
            pass
    
    def getSize(self):
        if self.state == "Human":
            size = 5
        elif self.state == "Vampire":
            size = 10
        else:
            SystemError
        return size

    def getColor(self):
        if self.state == "Human":
            color = "green"
        elif self.state == "Vampire":
            color = "red"
        else:
            SystemError
        return color

    def interaction(self, other):
        if self.state == "Human" and other.state == "Human":
            if random.random() < 0.4:
                self.health += 20
                other.health -= 20
            else:
                self.health += 10
                other.health += 10
        if self.state == "Human" and other.state == "Vampire":
            if random.random() < 0.7:
                self.state = "Vampire"
            else:
                other.health = 0
        if self.state == "Vampire" and other.state == "Vampire":
            self.health -= 20
            other.health -= 20

class Item:
    def __init__(self, pos, state):
        self.pos = pos
        self.state = state

    def __str__(self):
        return self.state + " @ " + str(self.pos)

    def getSize(self):
        if self.state == "Water":
            size = 10
        elif self.state == "Food":
            size = 5
        elif self.state == "Garlic":
            size = 5
        else:
            SystemError
        return size

    def getColor(self):
        if self.state == "Water":
            color = "blue"
        elif self.state == "Food":
            color = "brown"
        elif self.state == "Garlic":
            color = "grey"
        else:
            SystemError
        return color

    def interaction(self, character):
        if character.state == "Human":
            if self.state == "Water":
                character.health += 50
            elif self.state == "Food":
                character.health += 30
            elif self.state == "Garlic":
                character.health += 100
            else:
                SystemError