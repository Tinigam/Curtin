#Type in Animal class
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
	
class Shelter():
	def __init__(self, name, address, phone):
		self.name = name
		self.address = address
		self.phone = phone
		self.processing = []
		self.available = []
		self.adopted = []

	def newAnimal(self, type, name, dob, colour, breed):

		temp = None
		if type == 'Dog':
			temp = Dog(name, dob, colour, breed)
		elif type == 'Cat':
			temp = Cat(name, dob, colour, breed)
		elif type == 'Bird':
			temp = Bird(name, dob, colour, breed)
		else:
			print('Error, unknown animal type: ', type)

		if temp:
			self.processing.append(temp)
			print('Added ', name, ' to processing list')

	def makeAvailable(self, name):
		for animal in self.processing:
			if(animal.name == name):
				self.available.append(animal)
				self.processing.remove(animal)

	def makeAdopted(self, name):
		for animal in self.available:
			if(animal.name == name):
				self.adopted.append(animal)
				self.available.remove(animal)

	def displayProcessing(self):
		print("Display Processing")
		for animal in self.processing:
			animal.printit()

	def displayAvailable(self):
		print("Display Available")
		for animal in self.available:
			animal.printit()

	def displayAdopted(self):
		print("Display Adopted")
		for animal in self.adopted:
			animal.printit()

	def displayAll(self):
		self.displayProcessing()
		print()
		self.displayAvailable()
		print()
		self.displayAdopted()
