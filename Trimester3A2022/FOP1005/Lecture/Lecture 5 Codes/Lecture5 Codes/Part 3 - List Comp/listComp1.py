numbers = [1, 2, 3, 4, 5]
doubled_numbers = []
for n in numbers:
	doubled_numbers.append(n * 2)
print(doubled_numbers)

print()
doubled_numbers = [n * 2 for n in numbers]
print(doubled_numbers)