# def e_potentielle(masse, hauteur, e_limite, g=9.81):
#     E = masse * hauteur * g
#     if (E <= e_limite):
#         print(E, 'joules')
#     else:
#         print(E, 'est superieure a la limite')

# res = e_potentielle(80, 5, 6000)

# def e_potentielle_limite(masse, hauteur, e_limite, g= 9.81):
#     E = masse * hauteur * g
#     print(E)
#     return E < e_limite


# res1 = e_potentielle_limite(80, 5, 4000)
# print(res1)

# f = lambda x, y: x**2 + y
# print(f(2, 1))

def e_pot(masse, hauteur, e_limite, g = 9.81):
    E = masse * hauteur * g
    if (E <= e_limite):
        print(E, "joules")
    return E

e_pot(80, 5, 4000, 9.81)

        

