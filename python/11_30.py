import numpy as np
#  indexing
# A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(A)
# print(A[0, 1])

# slicing
# print(A[:, 0])
# print(A[0, :])
# subsetting

# B = A[0:2, 0:2]
# print(B)
#  changer les values de A
# A[0:2, 0:2] = 10
# print(A)

# C = A[0:3, 1:3]
# print(C)

# D = A[:, -2:]
# print(D)

# B = np.zeros((4,4))
# print(B)

# B[1:3, 1:3] = 1
# print(B)

# C = np.zeros((5, 5))
# print(C)
# C[::2, ::2] = 1
# print(C)

# boulean indexing

# A = np.random.randint(0, 10, [5, 5])
# print(A)
# print( A < 5)

# A[A < 5] = 10
# print(A)

from scipy import misc
import matplotlib.pyplot as plt
face = misc.face(gray = True)
plt.imshow(face, cmap=plt.cm.gray)
plt.show()
print(face.shape)
h = face.shape[0]
w = face.shape[1]
# zoom = face[192:576, 256:768]
zoom = face[h//4:-h//4, w//4:-w//4]
zoom[zoom > 150] = 255
plt.imshow(zoom, cmap=plt.cm.gray)
plt.show()






