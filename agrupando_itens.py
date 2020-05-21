from operator import itemgetter;
from itertools import groupby;

exemplos = [('marcos', 28), ('pedro', 19), ('joao', 20), ('marcos', 20), ('joao', 18), ('marcos', 30)]

print (f'Exemplos: {exemplos}')

# Ordenar pelo nome
exemplos.sort(key=itemgetter(0))
print(exemplos)

# Agrupando pela Chave
print({ key: sorted(map(itemgetter(1), value)) for key, value in groupby(exemplos, key=itemgetter(0) )})