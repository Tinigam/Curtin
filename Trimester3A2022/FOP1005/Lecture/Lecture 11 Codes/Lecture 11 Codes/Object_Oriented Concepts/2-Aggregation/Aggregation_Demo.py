class Car():

	def __init__(self, driver, passengers):
		self.driver = driver
		self.passengers = passengers

	def printit(self):
		print(self.driver)
		for passenger in self.passengers:
			print(passenger)


class Person:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.name


if __name__ == "__main__":

	driver = Person("Driver")
	p1 = Person("P1")
	p2 = Person("P2")
	passengers = [p1, p2]

	car = Car(driver, passengers)
	car.printit()

	#destroy car
	car = None
	print(car)
	#objects create in car are destroyed as well
	print(driver)
	for p in passengers:
		print(p)
