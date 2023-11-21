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