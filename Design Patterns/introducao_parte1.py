class Pessoa(object):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def obter_pessoa(self):
        return '<Pessoa (%s, %s)>' % (self.nome, self.idade)

p = Pessoa('Marcos', 28)
print('Tipo de objeto: ', type(p), 'Memoria: ', id(p))