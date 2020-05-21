from operator import itemgetter

lista = [{'idade': 28}, {'idade': 15}, {'idade': 20}]

print(f'Lista: {lista}')

# Mostra a menor idade
menor = min(lista, key=itemgetter('idade'))
print(f'Menor idade: {menor}')

# Mostra a maior idade
maior = max(lista, key=itemgetter('idade'))
print(f'Maior idade: {maior}')