#  data structures: sequences : list, tuple or string
#  list[] can be filled with int char etc.
#  tuple() is fixed, it is safe and can be quicker than list
#  string''

# indexing [0] first element of the sequences
# [1] secound
# -1 is the last one
# -2 is the secound last

# slicing : like the range function with args: (start, end, path)
# slicing can be used to change a sequence as well
# ex: print(villes[0:3])
# print(villes[:3])
# print(villes[3:])
# print(villes[1:3:2])
# print(villes[::2]) print tous les elements de la liste du debut a la fin tous les deux elts

# actions or methods we can do on a list

# villes  = ['paris', 'berlin', 'londres', 'bruxelles']

# append: add an at the end of the list
# villes.append('dublin')

# insert: takes two args : index where to addup arg2
# villes.insert(2, 'madrid')

# insert: alloow to add a list to a list
# villes_2  = ['amsterdam', 'rome']
# villes.extend(villes_2)

# len(list): nbr of element

# sort: sort in alphabetic order
# villes.sort()
# villes.sort(reverse=true) => sort in reverse order

# count(value): tells us number of occurence of tha value in the list
# villes.count('paris')

# pop, ...


# for index, valeur in enumerate(villes):
#      print(index, valeur)

# liste_2 = [2, 3, 24]
# for a, b in zip(villes, liste_2):
#      print(a, b)


def fibo(n):
    a = 0
    b = 1
    list = []
    while(a< n):
        list.append(a)
        a, b = b, a+b
    for i in list:
        print(i)
    for index, value in enumerate(list):
        print(index, value)
    return list
    
# def fibo(n):
#     a = 0
#     b = 1
#     list = [] 
#     while (a < n):
#         print(a)
#         list.append(a)
#         a, b = b, a+b
#     for i in list:
#         print(i)      
#     for index, valeur in enumerate(list):
#             print(index, valeur)

fibo(5)
