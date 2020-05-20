# conjunto ou sets não permite repetidos
c = {1, 2, 3, 4, 5}
d = {3, 3, 4, 4, 6, 7}
print(f'Conjunto C: {c}')
print(f'Conjunto D: {d}')

# União de conjuntos
print(f'Uniao dos conjuntos c | d: ', c | d)

# Interseccao dos elementos (comum em C e D)
print(f'Intersecao dos conjuntos c & d: ', c & d)

# Elementos que em C, mas não estão d
print(f'Elementos que em C, mas nao estao d (c - d): ', c - d)

# Elemento que estão em C ou em D, mas não estão em Ambos.
print(f'Elemento que estao em C ou em D, mas nao estao em Ambos. (c ^ d): ', c ^ d)