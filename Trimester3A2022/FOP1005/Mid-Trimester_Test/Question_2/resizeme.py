import numpy as np 
data = np.zeros((5,2,2)) 
data[0,1,1] = 17 
data[4,1,0] = 9 
print(data) 
data.resize(2,10) 
print(data)