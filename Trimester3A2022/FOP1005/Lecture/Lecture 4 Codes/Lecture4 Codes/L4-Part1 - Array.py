import numpy as np

listarray = np.array([1, 2, 3, 4]) # From a list
emptyarray = np.empty(100) # Empty array, or is it?
#with some "random" number - the leftover data in the RAM previouly
print(emptyarray)

print()
zeroarray = np.zeros(100)         # Array of 100 zeros - float
print(zeroarray)

print()
onesarray = np.ones(100)          # Array of 100 ones - float
print(onesarray)

print()
randomarray = np.random.rand(100) # Array of 100 random numbers 0<=x<1
print(randomarray)

print()
arangearray = np.arange(0, 20, 2) #Array range - from 0 to 20-1 with step of 2
print(arangearray)

print()
linarray = np.linspace(0, 1, 6) #6 evenly spread numbers between 0 to 1
print(linarray)

print()
linarray = np.linspace(0, 1, 5, endpoint=False)
#5 evenly spread numbers between 0 to 1(exclude)
print(linarray)

print()
#Accessing elements
listarray = np.array([1, 2, 3, 4])
print(listarray[0]) #access item index 0 in array listarray
r = listarray[2] + listarray[3] # 3+4=7
print(r)

print()
#Looping through elements
listarray = np.array([1, 2, 3, 4])
for index in range(len(listarray)):
	print(listarray[index])

print()
for value in listarray:
	print(value)

#Slicing
listarray = np.array([1, 2, 3, 4])
print(listarray[1:3]) #index 1 to 3-1
print(listarray[:3])  #index 0 to 3-1
print(listarray[1:])  #index 1 to the end
print(listarray[::-1]) #index the end to 0, step of -1 i.e. reverse




