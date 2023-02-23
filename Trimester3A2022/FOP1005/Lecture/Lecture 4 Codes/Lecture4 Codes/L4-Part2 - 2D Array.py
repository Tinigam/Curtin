import numpy as np

#Building 2D array from lists:
listarray = np.array([[1, 2], [3, 4]]) #list within list
print(listarray)

print()
list1 = [5, 6]
list2 = [7, 8]
listarray = np.array([list1, list2])#list within list
print(listarray)

print()
#Initialised with 0 values:
zeroarray = np.zeros((10, 10)) #(10,10) is the 2D array size
print(zeroarray)

print()
#Initialised with 1 values:
onesarray = np.ones((10, 10)) #(10,10) is the 2D array size
print(onesarray)

print()
#Meshgrid functions
#Create an array of integers, going from 0 to 4 across each dimension
y, x = np.mgrid[0:5, 0:5]
print(y)
print()
print(x)

print()
#Print the contents of an array
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)

#Get the total number of entries in an array
size = np.size(a) # 6
print(size)
#get the dimensions of an array
shape = np.shape(a) # (2,3)
print(shape)
#Get the length of the first dimension in an array
length = len(a) # 2
print(length)

print()
#Reshaping arrays
a = np.array([[1, 2, 3], [4, 5, 6]])
print(np.shape(a))    # (2,3)
print(np.size(a))    # 6
d = a.reshape(3, 2)
print(d)
d = a.reshape(1, 6)
print(d)
d = a.reshape(6, 1)
print(d)

print()
listarray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
n1 = listarray[0, 0] #is 1
print(n1)
n2 = listarray[2, 0] #is 7
print(n2)
n3 = listarray[1, 2] #is 6
print(n3)

print()
numarray = np.array([[1, 2, 3, 4], [5, 6, 7, 8],
                     [9, 10, 11, 12]])
print('Shape is: ', np.shape(numarray)) 		# (3,4)
print('Number of rows: ', len(numarray[:, 0])) 	# 3
print('Number of cols: ', len(numarray[0, :]))	# 4

row, col = 0, 0
while row < len(numarray[:, 0]):
	while col < len(numarray[0, :]):
		print('Element [', row, ',', col, '] is: ', numarray[row, col])
		col = col + 1
	row = row + 1
	col = 0

print()
#Looping in a Pythonic way...
for row in numarray:
	for element in row:
		print('Element:', element)

print()
#To access the indexes, use enumerate...
for rindex, row in enumerate(numarray):
	for cindex, element in enumerate(row):
		print('Element: [', rindex, ',', cindex, '] is :', element)

print()
#Slicing 2-D Arrays
listarray = np.array([[1, 2, 3, 4],
                      [5, 6, 7, 8],
                      [9, 10, 11, 12]])
#    0  1  2  3
# 0 [1, 2, 3, 4]
# 1 [5, 6, 7, 8]
# 2 [9, 10, 11, 12]

a = listarray[1:, 0] # row index 1 to the end, col index 0
print(a)
a = listarray[2, 1:] #row index 2, col index 1 to the end
print(a)
a = listarray[2, :]  #row index 2, col index 0 to the end
print(a)
a = listarray[:, ::2] #row index 0 to the end, col index 0 to the end step of 2
print(a)

