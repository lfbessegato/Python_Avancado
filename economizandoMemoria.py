class Pessoa:
    __slots__ = ['nome', 'idade', 'peso'] # Cria reduzido o array
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso