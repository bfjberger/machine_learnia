# https://docs.python.org/3/library/functions.html
# built-in functions in python 

# x = -3
# print(abs(x))

# x = 5.14
# print(round(x))

# list_1 = [0 , 23, 14, -19]

# print(max(list_1))
# print(min(list_1))
# print(len(list_1))
# print(sum(list_1))

# x = 
# print(type(x))
# x = str(x)
# print(type(x))
# y = '20'

# y = int(y)
# print(type(y))

# x = input('please enter an int')
# print(x) 
# print(type(x))

# x = 32
# ville = 'London'
# message = "la temperature est de {} degC a {}".format(x, ville)
# print(message)

# x = 32
# ville = 'London'
# message = f"la temperature est de {x} degC a {ville}"
# print(message)

# import numpy as np

# parametres = {
#     "W1": np.random.randn(2, 4),
#     "b1": np.zeros((2, 1)),
#     "W2": np.random.randn(2, 2),
#     "b2": np.zeros((2, 1))
# }

# for i in range(1, 3):
#     print("couche", i)
#     print(parametres["W{}".format(i)])


# f = open('fichier.txt', 'w')
# f.write('bonjour')
# f.close()

# f = open('fichier.txt', 'r')
# print(f.read())
# f.close()

# with open('fichier.txt', 'w') as f:
#     for i in range(10):
#         f.write("{}^2 = {}\n".format(i, i**2))

# with open('fichier.txt', 'r') as f:
#     liste = f.read().splitlines()
#     print(liste)

# liste = [line for line in open('fichier.txt', 'r')]
# print(liste)

# liste = [line.strip() for line in open('fichier.txt', 'r')]
# print(liste)

# x = int(input("Please enter a number\n"))
# y = input("Please enter a city name\n")

# message = "The number written is {} and the city name is {}".format(x, y)
# print(message)


# with open('fichier.txt', 'w') as f:
#     for i in range(10):
#         f.write("{}^2 = {}\n".format(i, i**2))

# with open('fichier.txt', 'r') as f:
#     list_file = []
#     for line in f:
#         list_file.append(line.strip())
# print(list_file)

with open('fichier.txt', 'w') as f:
    for i in range(10):
        f.write("{}^2 = {}\n".format(i, i**2))

with open('fichier.txt', 'r') as f:
    list_file = []
    list_file = f.readlines()
print(list_file)