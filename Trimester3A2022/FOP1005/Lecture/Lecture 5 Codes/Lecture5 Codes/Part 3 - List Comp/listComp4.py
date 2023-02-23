# create list of first 10 square numbers
squares = []
for s in range(1, 11):
	squares.append(s * s)
print(squares)

print()
numbers = list(range(1, 11))
squares = [s * s for s in numbers]
print(squares)

print()
squares = [s * s for s in range(1, 11)]
print(squares)