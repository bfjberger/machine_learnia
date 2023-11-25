import numpy as np

# np.random.seed(0)
# A = np.random.randint(0, 10, [5, 5])
# print(A)
# print(A.sum())
# print(A.sum(axis = 1))
# print(A.mean())
# print(A.std())
# print(A.var())
# print(np.corrcoef(A)[0,1])
# values, counts = np.unique((A), return_counts=True)
# print(values)
# print(counts)
# print(values[counts.argsort()])
# for i, j in zip(values[counts.argsort()], counts[counts.argsort()]):
#     print(f'valeur {i} apparait {j}')

np.random.seed(0)
A = np.random.randint(0, 100, [10, 5])
print(A)
D = (A - A.mean(axis = 0)) / A.std(axis=0)
print(D)





