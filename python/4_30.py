def fibo(n):
    a = 0
    b = 1
    list = [] 
    while (a < n):
        print(a)
        list.append(a)
        a, b = b, a+b
    for i in list:
        print(i)      
    for index, valeur in enumerate(list):
            print(index, valeur)

fibo(5)
