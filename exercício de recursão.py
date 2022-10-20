#exercício de recursão
''' questão 1
def potencia(x, y):
    if y == 0:
        return 1
    else:
        return x * potencia(x, y-1)
    
print(potencia(2,3))
'''
''' questão 2
def fatorial(n):
    if n == 1:
        return 1
    else:
        return n *fatorial(n-1)

print(fatorial(0))

'''

'''#questão 3
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(7))
print(fibonacci(9))

'''
