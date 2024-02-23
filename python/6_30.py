# list comprehension: is a way to write a for condition in the list itself in order to save TimeoutError

# list = []
# for i in range(10):
#     list.append(i**2)
    
# list_2 = [i**2 in range(10)]

# list_1 = []
# for i in range (10):
#     list_1.append(i**2)

# print(list_1)

# list_2 = [i**2 for i in range(10)]
# print(list_2) 

# list_3 = [[i for i in range(3)] for j in range(4)]
# print(list_3)

# dictionnaire={ 
#      '0':'Pierre',
#      '1':'Jean',
#      '2':'Julie',
#      '3':'Sophie'
# }

# prenoms = ['Pierre', 'Jean', 'Julie', 'Sophie']

# dico = {k:v for k, v in enumerate(prenoms)}
# print(dico)
# print(dico.keys())
# print(dico.values())

# ages = [24, 62, 10, 23]
# dico_2 = {prenom:age for prenom, age in zip(prenoms, ages) if age >20}
# print(dico_2)

# tuple_1  = tuple((i**2 for i in range(10)))
# print(tuple_1)

carre = {
    str(k):k**2 for k in range(0, 20)
}

print(carre)
