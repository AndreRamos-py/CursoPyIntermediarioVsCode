"""
Retorno de valores das funções (return)
"""

def soma(x, y):
    if x > 10:
        return [10, 20]
    return x + y


soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1)
print(soma2)
print(soma(11, 55))
#-------------------------------------#
numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
outra_soma = soma(*numeros)
print(outra_soma)

print(sum(numeros))
