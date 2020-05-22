lista = [10, 5, 20, 8]
print(f'Lista: {lista}')

# Reduzindo dados
print(f'Soma: {sum(lista)}')
print(f'Maior: {max(lista)}')
print(f'Menor: {min(lista)}')

# Transformando dados

# Expressao geradora
soma_quad = sum(x * x for x in lista)
print(f'Soma dos Quadrado: {soma_quad}')