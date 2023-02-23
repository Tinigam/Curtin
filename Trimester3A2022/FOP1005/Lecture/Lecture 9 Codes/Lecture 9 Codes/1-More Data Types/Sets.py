#sets
letter = "a"
vowelcount = 0
vowels = 'aeiou'
if letter in vowels:
	vowelcount += 1

print(vowelcount)

print()
#Set creation and operations
pythonlist = ['John', 'Eric', 'Graham', 'Terry', 'Michael', 'Terry']
pythonset = set(pythonlist)
goodieslist = ['Bill', 'Graham', 'Tim']
goodiesset = set(goodieslist)
print(pythonset)
print(goodiesset)
print('Intersection = ', pythonset.intersection(goodiesset))
print('Union = ', pythonset.union(goodiesset))
print('Difference = ', pythonset.difference(goodiesset))
print('Difference = ', goodiesset.difference(pythonset))
