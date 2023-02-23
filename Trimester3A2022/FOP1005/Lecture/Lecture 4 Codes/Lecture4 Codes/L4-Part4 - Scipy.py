from scipy import misc
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt
import imageio

##show orignial
#face = misc.face()
#plt.imshow(face)
#plt.show()

##show gray
#face = misc.face(gray=True)
#plt.imshow(face)
#plt.show()

#face = misc.face(gray=True)
##https://matplotlib.org/stable/tutorials/colors/colormaps.html
#plt.imshow(face, cmap=plt.cm.gray) #colour map
#plt.show()

##show shifted face
#face = misc.face(gray=True)
#shifted_face = ndimage.shift(face, (50, 50))
#plt.imshow(shifted_face)
#plt.show()

##show rotated face
#face = misc.face(gray=True)
#rotated_face = ndimage.rotate(face, 30)
#plt.imshow(rotated_face)
#plt.show()

##show cropped face
#face = misc.face(gray=True)
#cropped_face = face[100:-100, 100:-100]
#plt.imshow(cropped_face)
#plt.show()

#show orignal face
face = misc.face(gray=True)
size1 = np.shape(face)  # (768, 1024)
print(size1)
plt.imshow(face)
plt.show()

#first pixelled face
pixel_face = face[::10, ::10]
size2 = np.shape(pixel_face)  # (77, 103)
print(size2)
plt.imshow(pixel_face)
plt.show()

#second pixelled face
pixel_face2 = face[::50, ::50]
size3 = np.shape(pixel_face2)  # (16, 21)
print(size3)
plt.imshow(pixel_face2)
