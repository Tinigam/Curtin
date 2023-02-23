#
# prettyface.py
#
import matplotlib.pyplot as plt
from scipy import ndimage
from scipy import misc

face = misc.face(gray=True)

face = ndimage.shift(face, (100, 50))
face = ndimage.rotate(face, 40)
face = face[200 : 1000, 200 : 500]
face = face[::10, ::10]

plt.imshow(face)
plt.imshow(face, cmap=plt.cm.gray)


plt.show()