#
# Name : Gao Yuyang
# ID   : 21297919
#
# heat.py - heat diffusion simulation
#
import numpy as np
import matplotlib.pyplot as plt

def calcheat(r, c):
    return 0.1 * (curr[r-1 : r+2, c-1 : c+2].sum() + curr[r,c])

size = 10 

curr = np.zeros((size,size)) 
print(curr)    

# create heat source
hlist = []
fileobj = open('/home/tinigam/Desktop/FOP1005/Prectice/Prec05/heatsource.csv','r')
for line in fileobj:
    line_s = line.strip()
    ints = [int(x) for x in line_s.split(',')]
    hlist.append(ints)
fileobj.close()
h = np.array(hlist, dtype=int)
curr = h.copy()

next = np.zeros((size,size)) 

for timestep in range(100): 
    for r in range(1, size-1): 
        for c in range (1, size- 1 ): 
            next[r,c] = calcheat(r, c)

    # for r in range(size): 
    #     for c in range(size):
    #         if h[r, c] > next[r, c]:
    #             next[r, c] = h[r, c]
    next = np.where(curr > next, h, next)
    curr = next.copy()

    print("Time step: ", timestep) 
    print(next)    
    curr = next.copy() 

plt.imshow(curr, cmap=plt.cm.hot) 
plt.show() 
