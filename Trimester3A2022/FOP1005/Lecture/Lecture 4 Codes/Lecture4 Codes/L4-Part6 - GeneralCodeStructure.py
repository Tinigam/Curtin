import matplotlib.pyplot as plt
import numpy as np
def calc_heat(row,col):
	subgrid = b[row-1:row+2,col-1:col+2]
	result = 0.1 * (subgrid.sum()+ b[row,col])
	return result

size = 10
b = np.zeros((size,size))
b2 = np.zeros((size,size))

for i in range(size):
	b[i,0] = 10
	
for timestep in range(5):
	for r in range(1, size-1):
		for c in range (1, size-1 ):
			b2[r,c] = calc_heat(r,c)
		for i in range(size):
			b2[i,0] = 10
		b = b2.copy()

plt.title('Heat Diffusion Simulation')
plt.imshow(b2, cmap=plt.cm.hot)
plt.show()

