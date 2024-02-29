# import matplotlib.pyplot as plt
# import numpy as np

# # x = np.linspace(0, 2, 10)
# # y = x**2
# # print(x)

# # plt.plot(x, y, c= 'black', lw=5, ls='--')
# # plt.show()

# # plt.scatter(x, y)
# # plt.show()

# # plt.figure()
# # plt.plot(x, y, label='quadratique')
# # plt.plot(x, x**3, label='cubique')
# # plt.title('figure 1')
# # plt.xlabel('axe x')
# # plt.ylabel('axe y')
# # plt.legend()
# # plt.show()

# # plt.savefig('figure.png')

# # plt.subplot(2, 1, 1)
# # plt.plot(x, y, c='red')
# # plt.subplot(2, 1, 2)
# # plt.plot(x, y, c='yellow')
# # plt.show()

# # fig, ax = plt.subplots()
# # ax.plot(x, y)
# # plt.show()

# dataset = {f"experience{i}":np.random.randn(100) for i in range(4)}
# def graphique(dataset):
#     n = len(dataset)
#     plt.figure(figsize=(12, 8))
#     for k, i in zip(dataset.keys(), range(1, n+1)):
#         plt.subplot(n, 1, i)
#         plt.plot(dataset[k])
#         plt.title(k)
#         plt.xlabel('axe x')
#         plt.ylabel('axe y')
# graphique(dataset)        
# plt.show()

# import numpy as np

# x = np.linspace(0, 2, 10)
# y = x**2
# print(x)

# before plot , we have to make figure and define the size of it in inch
# plt.figure(figsize=(12, 8))
# we can add several plot to the same figure
# we can add a title with plt.title('figure 1')
# add a name to the axis plt.xlabel('axe x')
# plt.legend() plt.plot(x,y, label='quadratique')
# save the figure plt.savefig('fig.png')

# we can add parameter to plot
# choose line color c='red' => plt.plot(x, y, c='red')
# choose line thickness (epaisseur) lw=4 => plt.plot(x, y, c='red', lw=4)
# choose line style ls='--' => plt.plot(x, y, c='red', lw=4, ls='--')

# import matplotlib.pyplot as plt

# plt.figure(figsize=(12, 8))
# plt.plot(x, y)
# plt.show()

# plot several graph in the same fig using subplot

import numpy as np
import matplotlib.pyplot as plt

dataset = {f"experience{i}": np.random.randn(100) for i in range(4)}


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





