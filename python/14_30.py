import matplotlib.pyplot as plt
import numpy as np

# x = np.linspace(0, 2, 10)
# y = x**2
# print(x)

# plt.plot(x, y, c= 'black', lw=5, ls='--')
# plt.show()

# plt.scatter(x, y)
# plt.show()

# plt.figure()
# plt.plot(x, y, label='quadratique')
# plt.plot(x, x**3, label='cubique')
# plt.title('figure 1')
# plt.xlabel('axe x')
# plt.ylabel('axe y')
# plt.legend()
# plt.show()

# plt.savefig('figure.png')

# plt.subplot(2, 1, 1)
# plt.plot(x, y, c='red')
# plt.subplot(2, 1, 2)
# plt.plot(x, y, c='yellow')
# plt.show()

# fig, ax = plt.subplots()
# ax.plot(x, y)
# plt.show()

dataset = {f"experience{i}":np.random.randn(100) for i in range(4)}
def graphique(dataset):
    n = len(dataset)
    plt.figure(figsize=(12, 8))
    for k, i in zip(dataset.keys(), range(1, n+1)):
        plt.subplot(n, 1, i)
        plt.plot(dataset[k])
        plt.title(k)
        plt.xlabel('axe x')
        plt.ylabel('axe y')
graphique(dataset)        
plt.show()

