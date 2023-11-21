def sign(x):
    if (x > 0):
        print(x, 'positif')
    elif (x == 0):
        print(x, 'null')
    else:
        print(x, 'negatif')


print(sign(0))


for i in range(10, -10, -3):
    print(i)
    sign(i)    
    
def fibo(n):
    a = 0
    b = 1
    while (a < n):
        print(a)
        a, b = b, a+b
        
        
fibo(5)
