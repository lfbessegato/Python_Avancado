# Geradores são iterables quando pode percorrer os elementos dos geradores
lista = [1, 2, 3, 4, 5]
for i in lista:
    print(i)

# Exemplo
gerador = (letra for letra in 'python')
print(gerador.__next__())
print(next(gerador))