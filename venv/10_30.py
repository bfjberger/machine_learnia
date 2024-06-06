import numpy as np

#A is on object of np.array class. don t forget that [] is a tupple. so you can't change the size of your tupple 
# A = np.array([1, 2, 3])
# print(A.ndim)
# print(A.size)
# print(A.shape)

def initialization(m, n):
    matrix = np.random.randn(m, n)
    matrix = np.concatenate((matrix, np.ones((matrix.shape[0], 1))), axis = 1)
    print(matrix)

initialization(2, 3)