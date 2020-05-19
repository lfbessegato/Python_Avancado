
# Desempacotamento em Listas
x, y, z = [1,2,3]
print(x,y,z)

# Desempacotamento em Tuplas
n1, n2= ("Luciano", "joao")
print(n1, n2)

# Desempacotar Strings
a,b,c,d,e = 'HELLO'
print(a,b,c,d,e)

# Desempactar muitos valores com poucas variaveis
x, y, _ = [1, 2, 3]
print(x, y)

####################
lista = [9, 4, 5, 15, 20]
# *n1 -> Guarda os 4 primeiros elementos.
# *n2 -> Guarda os 4 ultimos elementos
# Utilidade desempacotar iteraveis de tamanhos desenconhecidos.
*n1, n2 = lista
print(n1, n2)

##################
# Exemplo descartar 1 primeira e ultima nota
notas = [9, 7, 8, 5, 10]
n1, *n2, n3 = notas
print(n2)

# Exemplo pegar a primeira e ultima nota
n1, *_, n3 = notas
print(n1)
print(n3)

