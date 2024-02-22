# dictionnaire: association key/Value
# it is not a sequence, there is no order 
# we can't have two identical keys, but you can have several time the same  value
# a dictionnaire can contain another dictionnaire
# often used to stock the neural network parametres
# traduction = {
#     "chien":"dog",
#     "chat":"cat"
# }

# dic methods:
# values: 
# inventaire.values()
# inventaire.keys()
# len(inventaire)

# add another association in the inventaire 
# inventaire['abricot'] = 12 (with a new key which is abricot and its value 12)

# list = ('paris', 'londres', 'bruxelles')
# inventaire.fromkeys(list)

# inventaire.pop() erase from a dict the key, it can be used to save it in a variable

# for k, v in inventaire.items():
#     print(k, v)


positif:[]
negatif:[]
classeur = 
{
    'positif',
    'negatif'
}
def trier(classeur, nombre):
    if (nombre >= 0):
        positif.append(nombre)
    else:
        negatif.append(nombre)
return classeur





# traduction = {
#     "chien":"dog",
#     "chat":"cat",
#     "souris":"mouse",
#     "oiseau":"bird"

# }

# inventaire = {
#     "bananes": 5000,
#     "pommes": 2094,
#     "poires": 412809,
#     "cerises": 2893
# }

# print(inventaire.values())
# print(inventaire.keys())
# print(len(inventaire))

# print(inventaire)
# inventaire["abricots"] = 4902
# print(inventaire)

# print(inventaire.get('cerises', 1))

# list_1 = ('Paris', 'Londres', 'Bruxelles')
# print(inventaire.fromkeys(list_1), 'default')

# fruits = inventaire.pop('abricots')
# print(fruits)

# print(inventaire)


# for k, v in inventaire.items():
#     print(k, v)

classeur = {
    "positif":[],
    "negatif":[],
}

def trier(classeur, nombre):
    if (nombre >= 0):
        classeur['positif'].append(nombre)
    else:
        classeur['negatif'].append(nombre)
    print(classeur['positif'])
    print(classeur['negatif'])

    return classeur

trier(classeur, -5)