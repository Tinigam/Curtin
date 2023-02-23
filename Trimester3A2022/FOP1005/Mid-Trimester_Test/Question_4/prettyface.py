## prettyface.py
import matplotlib.pyplot as plt
from scipy import ndimage
from scipy import misc

face = misc.face(gray=True) 
rotated_face = ndimage.rotate(face, 35)
cropped_face = rotated_face[25:, 15:]
sampled_face = rotated_face[::5,::5]
plt.imshow(face)

plt.imshow(face, cmap=plt.cm.gray)
plt.show()

plt.imshow(sampled_face, cmap=plt.cm.gray)
plt.show()