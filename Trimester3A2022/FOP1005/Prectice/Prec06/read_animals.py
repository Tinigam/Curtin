from animals import *

animal_list = []
with open("/home/tinigam/Desktop/FOP1005/Prectice/Prec06/animals.csv") as animals:
    for animal in animals:
        animal = animal.strip()
        animal_data = animal.split(",")
        # print(animal_data)
        animal_type = animal_data[0]
        animal_name = animal_data[1]
        animal_dob = animal_data[2]
        animal_colour = animal_data[3]
        animal_breed = animal_data[4]
        
        if animal_type == "Dog":
            pet = Dog(animal_name, animal_dob, animal_colour, animal_breed)
        elif animal_type == "Cat":
            pet = Cat(animal_name, animal_dob, animal_colour, animal_breed)
        elif animal_type == "Bird":
            pet = Bird(animal_name, animal_dob, animal_colour, animal_breed)
        animal_list.append(pet)

for pet in animal_list:
    pet.printit()
    print()