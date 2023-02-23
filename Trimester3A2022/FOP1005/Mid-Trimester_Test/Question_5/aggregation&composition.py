# Explain aggregation and composition with an example in the object relationship:

# Composition is a stronger type of relationship where one object contains another object, and the contained object does not have an independent existence outside of the container object.
    # Composition
    # • “has-a” or “whole-part” relationship
    # • UML: Shown with solid diamond beside container 
    # class
    # • e.g., Car “has-a” Wheel
    # • Strong lifecycle dependency between classes
    # • Car is not a car without four Wheels and an Engine
    # • When Car is destroyed, so are the Wheels and Engine
class Car:
    def __init__(self, engine, driver=None, passengers=[]):
        self.engine = engine
        self.driver = driver
        self.passengers = passengers

class Engine:
    def __init__(self, model):
        self.model = model

engine = Engine("V8")

# Aggregation is a type of relationship where one object is a container for another object, and the contained object has its own independent existence.
    # Aggregation
    # • Weaker form of composition, but is still “has-a” 
    # • UML: Shown with open/unfilled diamond beside container
    # • Lifecycle dependency usually not strong
    # • Car does not always have a driver
    # • When Car is destroyed driver and passengers are not Drivers can drive different car

class Person:
    def __init__(self, name):
        self.name = name

driver = Person("John")
passengers = [Person("Jane"), Person("Jack")]
car2 = Car(engine, driver, passengers)
