try:
	age = int(input("Please enter your age: "))
	if age < 0:
		raise ValueError(str(age) + " is not valid")
except ValueError as err:
	print("You entered incorrect age input:", err)
else:
	print("I see that you are", age, " years old.")
finally:
	print("It was really nice talking to you. Goodbye!")