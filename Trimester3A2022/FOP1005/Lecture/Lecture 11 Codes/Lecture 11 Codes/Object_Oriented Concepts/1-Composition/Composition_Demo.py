class Car():

	def __init__(self, engine_type, no_of_cylinders, hardness, resistance):
		self.engine = Engine(engine_type, no_of_cylinders)
		wheel1 = Wheel(hardness, resistance)
		wheel2 = Wheel(hardness, resistance)
		wheel3 = Wheel(hardness, resistance)
		wheel4 = Wheel(hardness, resistance)
		self.wheels = [wheel1, wheel2, wheel3, wheel4]

	def printit(self):
		print(self.engine)
		for wheel in self.wheels:
			print(wheel)


class Wheel():

	def __init__(self, hardness, resistance):
		self.hardness = hardness
		self.resistance = resistance

	def __str__(self):
		return str(self.hardness) + " " + str(self.resistance)


class Engine():

	def __init__(self, engine_type, no_of_cylinders):
		self.type = engine_type
		self.no_of_cylinders = no_of_cylinders

	def __str__(self):
		return str(self.type) + " " + str(self.no_of_cylinders)


if __name__ == "__main__":

	car = Car("A", 4, 2, 10)
	car.printit()

	#destroy car
	#objects create in car are destroyed as well
	car = None
	print(car)



