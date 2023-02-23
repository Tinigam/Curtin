#tuple example
tup1 = ('spam', 'eggs', 42)
tup2 = (1, 4, 9, 16, 25)
tup3 = "yes", "oui", "ja", "si"

print(tup1)
print(tup2)
print(tup3)

print()
#Tuples are sequences
print(tup1[2])
print(tup2[1:-1])

print()
for i in tup3:
	print(i)

print()
print(tup1 + tup2)

print()
print(tup1 * 2)

print()
print(len(tup2))