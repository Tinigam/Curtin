## zeros.py -creating and resizing an array
import numpy as np

print('\nZERO ARRAY\n')
zeroarray = np.zeros((4,4,4))
print('Zero array size: ', np.size(zeroarray))
print('Zero arrayshape: ', np.shape(zeroarray), '\n')

zeroarray[0,2,3] = 10
zeroarray[3,0,1] = 20
zeroarray[3,3,3] = 30

print(zeroarray)

zeroarray.resize((64, 1))
print('Zero array size: ', np.size(zeroarray))
print('Zero array shape: ', np.shape(zeroarray), '\n')

print(zeroarray)

zeroarray.resize((16, 4))
print('Zero array size: ', np.size(zeroarray))
print('Zero array shape: ', np.shape(zeroarray), '\n')

print(zeroarray)
