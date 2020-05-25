texto = ('arquivo.txt')
print(texto.endswith('.txt'))
print(texto.startswith('arquivo'))
print(texto.find('arq')) # Retorna a posição

# Expressões regulares
data = '25/05/2019'
import re
r = True if re.match(r'\d+/\d+/\d+', data) else False
print(r)
r = True if re.match(r'\d+/\d+/\d+', texto) else False
print(r)
