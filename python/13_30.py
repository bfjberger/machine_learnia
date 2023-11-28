import numpy as np

np.random.seed(0)
A = np.random.randint(0, 10, [4,1])
B = np.ones((1, 4))
print(A)
print(B)
print(A+B)