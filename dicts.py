

'''
pessoa = {
    'nome': 'André',
    'sobrenome': 'Ramos',
    'idade': 20,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}
# print(pessoa, type(pessoa))
print(pessoa['nome'])
print(pessoa['sobrenome'])

print()

for chave in pessoa:
    print(chave, pessoa[chave])
'''
# Manipulando chaves e valores em dicionários
pessoa = {}

##
##

chave = 'nome'

pessoa[chave] = 'André Luis'
pessoa['sobrenome'] = 'Ramos'

print(pessoa[chave])

print(pessoa)

print('-'*10)

pessoa[chave] = 'Eunice'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

print('-'*10)

#print(pessoa.get('sobrenome'))
if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])
