import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()

x = iris.data
y = iris.target
names = list(iris.target_names)

# print(f'x contient {x.shape[0]} exemples et {x.shape[1]} variables')
# print(f'il y a {np.unique(y).size} classes')

# plt.scatter(x[:, 0], x[:,  1], c=y)
# plt.show()

from mpl_toolkits.mplot3d import axes3d

# ax = plt.axes(projection='3d')
# ax.scatter(x[:, 0], x[:, 1], x[:, 2], c=y)
# plt.show()

# f = lambda x, y: np.sin(x) + np.cos(x + y)

# X = np.linspace(0, 5, 100)
# Y = np.linspace(0, 5, 100)

# X, Y = np.meshgrid(X,Y)
# Z = f(X, Y)
# # print(Z.shape)

# ax = plt.axes(projection='3d')
# ax.plot_surface(X, Y, Z, cmap='plasma')
# plt.show()

# plt.hist(x[:, 0], bins=30)
# plt.show()

n = x.shape[1]
plt.figure(figsize=(12, 8))
for i in range(n):
    plt.subplot(n//2, n//2, i+1)
    plt.scatter(x[:, 0], x[:, i], c=y)
    plt.xlabel('0')
    plt.ylabel(i)
plt.show()