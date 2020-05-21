import itertools
lista1 = [1,2,3]
lista2 = [4,5,6]

print(f'Lista 1: {lista1}')
print(f'Lista 2: {lista2}')

comb = itertools.chain(lista1, lista2)

# mostra o objeto
print(f'objeto: {comb}')

# Mostra a lista combinada
print(f'Lista combinada: {list(comb)}')