precos = {
    'iphone': 2500,
    'notebook': 2000,
    'mouse': 90,
    'teclado': 70
}

print(f'Dicionario: {precos}')

# Montar um dicionários com preços maiores que 100
precos2 ={key:value for key, value in precos.items() if value > 100}
print(f'Novo dicionario: {precos2}')