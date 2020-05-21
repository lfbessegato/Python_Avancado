from operator import itemgetter
linhas = [{'nome': 'marcos', 'idade': 28}, 
    {'nome': 'joao', 'idade': 19},
    {'nome': 'maria', 'idade': 20},
    {'nome': 'pedro', 'idade': 30}
]

print(f'Lista de Dicionario: {linhas}')

# ordenar pelo Nome e pela idade
linhas_pelo_nome = sorted(linhas, key=itemgetter('nome'))
print(f'Lista ordenada pelo Nome: {linhas_pelo_nome}')

linhas_pela_idade = sorted(linhas, key=itemgetter('idade'))
print(f'Lista ordenada pela idade: {linhas_pela_idade}')