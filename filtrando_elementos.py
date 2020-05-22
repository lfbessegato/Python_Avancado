lista = [10, -5, 20, 30, -40, 100]

print(f'Lista: {lista}')

# ordenando por ordem crescente
p = (i for i in lista if i > 0)
print(p)

for j in p:
    print(j)