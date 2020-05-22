from collections import ChainMap
a = {'x':1, 'z':3}
b = {'y':2, 'z':4}

print(f'Mapeamentos a e b: {a} {b}')

# Combinando Mapeamento
# ChainMap utiliza os dicts originais
c = ChainMap(a, b)
print(f'Mapeamento combinado: {c}')

# Combinando o mapeamento criando um dicionário objeto
# Não reflete no dicionário combinado, update nos dict originais.
merged = dict(b)
merged.update(a)
print(f'Mapeamento combinado: {merged}')
