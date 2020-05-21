d = {'tablet': 2000, 'notebook': 3000, 'iphone': 5000}
print(f'Dicionario: {d}')

# Mostra o menor preço, utilizado a função zip para inverter os valores
min_preco = min(zip(d.values(), d.keys()))
print(f'Menor Preco e o produto: {min_preco}')


# Mostra o maior preço, utilizado a função zip para inverter os valores
max_preco = max(zip(d.values(), d.keys()))
print(f'Maior Preco e o produto: {max_preco}')


