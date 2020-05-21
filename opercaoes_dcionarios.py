d = {'marcos': 28, 'joao': 30, 'maria': 25}
d2 = {'jose': 18, 'joao': 19, 'marcos': 25}

# Mostra os dicionarios
print(f'Dicionario 1: {d}')
print(f'Dicionario 2: {d2}')

# Mostra as chaves dos dicionários
print(f'Keys do dicionario 1: {d.keys()}')
print(f'keys do dicionario 2: {d2.keys()}')

# Mostra as chaves em comum entre os dicionarios
print(f'Chaves comuns entre o dcionario 1 e o dicionario2: {d.keys() & d2.keys()}')

# Mostra as chaves que está no d1 mas não está em d2
print(f'Chaves que estao no dcionario 1 e nao no dicionario2: {d.keys() - d2.keys()}')