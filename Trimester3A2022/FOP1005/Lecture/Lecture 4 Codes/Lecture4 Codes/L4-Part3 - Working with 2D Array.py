import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])

#Operations
c = a + b # array([[ 8,10,12],[14,16,18]])
print(c)
c = a + 1 # array([[2,3,4],[5,6,7]])
print(c)
c = a - b # array([[-6,-6,-6],[-6,-6,-6]])
print(c)
c = a * b # array([[7,16,27],[40,55,72]])
print(c)
c = a / b # array([[0.142,0.25,0.333],[0.4,0.454,0.5]])
print(c)

print()
#Comparisons
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])
d = a < b
print(d)

print()
#Element-wise Functions
a = np.array([[1, 2, 3], [4, 5, 6]])
c = np.sqrt(a)
print(c)
c = np.sin(a)
print(c)

print()
#Array-wise Functions
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])
print(a.sum())
print(a.min())
print(a.max())
print(a.mean())

print()
print(a[:, 0])
print(a[:, 0].sum())
print(a[1, :])
print(a[1, :].sum())

print()
#Matrices in NumPy
a = np.matrix([[1, 2], [2, 3]])
b = np.matrix('1 -2; 2 3')
print(a)
print(b)

print()
#matrix operation
r = a + b
print(r)
r = c = 5 * a
print(r)
r = a * b
print(r)
r = a**-1
print(r)

print()
#Compute the determinant of the matrix
#https://www.mathsisfun.com/algebra/matrix-determinant.html
r = np.linalg.det(a) #-1
print(r)
#matrix transpose
#https://www.mathsisfun.com/definitions/transpose-matrix-.html
r = b.T
print(r)

#matrix eigenvalue and eigenvector
#https://www.mathsisfun.com/algebra/eigenvalue.html
e_val, e_vect = np.linalg.eig(a)
print(e_val)
print(e_vect)

