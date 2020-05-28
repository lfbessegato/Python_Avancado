# Exemplo de Herança
class Pai:
    def pai(self):
        print('oi, sou a classe pai')

class Filha(Pai):
    def filha(self):
        print('oi, sou a classe filha')

filha = Filha()
print(filha.pai())

# Abstração
class Adiciona:
    def __init__(self):
        self.soma = 0
    def adiciona(self, valor):
        self.soma += valor

ad = Adiciona()
for i in range(10):
    ad.adiciona(i)
print(ad.soma)


# Exemplo de composição
class A(object):
    def a1(self):
        print('a1')

class B(object):
    def b(self):
        print('b')
        A().a1()

objB = B()
objB.b()
