from collections import defaultdict
d = defaultdict(list)

# chave mapeando para vários valores
d['marcos'].append(10)
d['marcos'].append(20)
d['marcos'].append(30)
print(d['marcos'])

# outra chave mapeando para vários valores
d['joao'].append(1) 
d['joao'].append(2)
print(d['joao'])
