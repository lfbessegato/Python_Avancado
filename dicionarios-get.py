d = {'marcos': 28, 'joao':19, 'maria':25}
print(d)

# mostrar o valor de uma chave qualquer
print(d['marcos'])

# Mostra erro quando tenta mostrar o valor de uma chave inexistente print(d['luciano'])

# Utilizando o método get para obter o valor de uma chave existente
print(d.get('joao'))


# utilizando o método get para obter o valor de uma chave inexistente
if d.get('luciano'): 
    print('Chave inexistente')
else: 
    print ('chave existente.')

