#write the classes
class Dog():
    myclass = "Dog"
    def __init__(self, name, dob, colour, breed):
        self.name = name
        self.dob = dob
        self.colour = colour
        self.breed = breed
    def printit(self):
        print('Name: ', self.name)
        print('DOB: ', self.dob)
        print('Colour: ', self.colour)
        print('Breed: ', self.breed)
        print('Class: ', self.myclass)

class Cat():
    myclass = "Cat"
    def __init__(self, name, dob, colour, breed):
        self.name = name
        self.dob = dob
        self.colour = colour
        self.breed = breed
    def printit(self):
        print('Name: ', self.name)
        print('DOB: ', self.dob)
        print('Colour: ', self.colour)
        print('Breed: ', self.breed)
        print('Class: ', self.myclass)

class Bird():
    myclass = "Bird"
    def __init__(self, name, dob, colour, breed):
        self.name = name
        self.dob = dob
        self.colour = colour
        self.breed = breed
    def printit(self):
        print('Name: ', self.name)
        print('DOB: ', self.dob)
        print('Colour: ', self.colour)
        print('Breed: ', self.breed)
        print('Class: ', self.myclass)

if __name__ == "__main__":
    dog = Dog("Hugo", "1/1/2022", "Black", "Lab")
    dog.printit()
    cat = Cat("Hello", "1/1/1990", "Pink", "Kitty")
    cat.printit()
    bird = Bird("BigBird", "31/12/1990", "yellow", "Unknown")
    bird.printit()
