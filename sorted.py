class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def __repr__(self):
        return self.nome

# Função sorted -> retorna uma lista ordenada
lista = [10, 5, 11, 3, 20, 18]
print(sorted(lista))

# Ordenar uma tupla
tupla = ('python', 'java', 'haskell')
print(sorted(tupla))

#Ordenando um dicionário pelas chaves
d = {1: 'b', 2:'a', 3:'c'}
print(sorted(d))

# ordenando pelo nome da pessoa
def pelo_nome(pessoa):
    return pessoa.nome

# ordenando pela Idade da pessoa
def pela_idade(pessoa):
    return pessoa.idade

p1 = Pessoa('Marcos', 28)
p2 = Pessoa('Joao', 30)
p3 = Pessoa('Ana', 25)

pessoas = [p1, p2, p3]
print(sorted(pessoas, key=pelo_nome))
print(sorted(pessoas, key=pela_idade))

# Ordenando pela ordem inversa
print(sorted(pessoas, key=pela_idade, reverse=True))