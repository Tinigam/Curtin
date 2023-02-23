
import numpy as np
import matplotlib.pyplot as plt

##contour plot
#def f(x, y):
	#return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)


#n = 256
#x = np.linspace(-3, 3, n)
#y = np.linspace(-3, 3, n)
#X, Y = np.meshgrid(x, y)

#plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap='jet')
##plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap='hot')
#plt.contour(X, Y, f(X, Y), 8, colors='black')
#plt.show()


#Scatter plot
import numpy as np
import matplotlib.pyplot as plt
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colours = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N)) ** 2
plt.scatter(x, y, s=area, c=colours, alpha=0.5)
plt.show()


#import matplotlib.pyplot as plt
#import numpy as np
#def calc_heat(row,col):
	#subgrid = b[row-1:row+2,col-1:col+2]
	#result = 0.1 * (subgrid.sum()+ b[row,col])
	#return result

#size = 10
#b = np.zeros((size,size))
#b2 = np.zeros((size,size))

#for i in range(size):
	#b[i,0] = 10

#for timestep in range(5):
	#for r in range(1, size-1):
		#for c in range (1, size-1 ):
			#b2[r,c] = calc_heat(r,c)
		#for i in range(size):
			#b2[i,0] = 10
		#b = b2.copy()

#plt.title('Heat Diffusion Simulation')
#plt.imshow(b2, cmap=plt.cm.hot)
#plt.show()


