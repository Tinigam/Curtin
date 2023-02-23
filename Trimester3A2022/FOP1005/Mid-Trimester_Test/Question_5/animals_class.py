class Animal:
	myclass = "Animal"

	def __init__(self, name, dob, colour, breed):
		self.name = name
		self.dob = dob
		self.colour = colour
		self.breed = breed
		
	def __str__(self):
		return self.name + "|" + self.dob + "|" + self.colour + "|" + self.breed

	def printit(self):
		print("Name: ", self.name)
		print("Date of Birth: ", self.dob)
		print("Colour: ", self.colour)
		print("Breed: ", self.breed)

#Type in Dog, Cat and Bird class
class Cat(Animal):
	myclass = "Cat"

class Dog(Animal):
	myclass = "Dog"

class Bird(Animal):
	myclass = "Bird"

# The Animal class is a base class that defines certain attributes and behaviors that are common to all animals, such as a name, dob, colour, and breed.
# The Cat, Dog, and Bird classes are derived classes that inherit from the Animal class. 

dude = Dog('Dude', '1/1/2011', 'Brown', 'Jack Russell')
# In this code, a new Dog object is being created using the Dog class's constructor method.
# The Dog object being created has the name "Dude", date of birth "1/1/2011", colour "Brown", and breed "Jack Russell".
# It will have all of the attributes and behaviors of the Animal class, as well as any additional attributes or behaviors defined in the Dog class.
