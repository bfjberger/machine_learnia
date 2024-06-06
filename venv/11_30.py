import numpy as np

# A = np.array([[1,2,3], [4,5,6], [7,8,9]])
# B = A[:, -2:]

# # C = np.zeros((4, 4))
# # print(C)

# # C[1:3, 1:3] = 1'
# C = np.zeros((5,5))
# C[::2, ::2] = 1
# print(C)

from scipy import misc
import matplotlib.pyplot as plt


# face = misc.face()
# plt.imshow(face)
# plt.show()
# print(face.shape)


face = misc.face(gray=True)
plt.imshow(face, cmap=plt.cm.gray)
l = face.shape[0]
c = face.shape[1]
zoom_face= face[l//4: -l//4, c//4:-c//4]
zoom_face[zoom_face > 200] = 255
zoom_face[zoom_face < 90] = 0
plt.imshow(zoom_face, cmap=plt.cm.gray)
plt.show()

