from itertools import compress

nomes = ['marcos', 'joao', 'maria', 'pedro']
cont = [10, 5, 6, 2]
print(f'Listas: {nomes} {cont}')

# retorna maiores de 5
mais5 = [i > 5 for i in cont]
print(f'Maiores que 5: {mais5}')

print(list(compress(nomes, mais5)))

