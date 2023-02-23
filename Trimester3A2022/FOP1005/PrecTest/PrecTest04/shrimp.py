import random

class Shrimp():
    
    def __init__(self, pos, mapSize):
        # The position of the shrimp as x & y values stored in a list
        self.pos = pos
        self.mapSize = mapSize
    
    def stepChange(self):
        self.pos[0] += random.randint(-10, 10)
        self.pos[1] += random.randint(-10, 10)

        # If the shrimp moved off the map, move it back on
        if self.pos[0] < 0:
            self.pos[0] = 0
        elif self.pos[0] >= self.mapSize[0]:
            self.pos[0] = self.mapSize[0]
        
        if self.pos[1] < 0:
            self.pos[1] = 0
        elif self.pos[1] >= self.mapSize[1]:
            self.pos[1] = self.mapSize[1]