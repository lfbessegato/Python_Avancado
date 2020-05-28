class MeuInt(int):
    def __add__(self, num):
        return 0

a = MeuInt(1)
print(a + 2)

# OverWrite do append
class MinhaLista(list):
    def append(self, *args):
        self.extend(args)

l = MinhaLista()
l.append(1)
l.append(2,3,4,5,6,7)
print(l)

class MyList(list):
    def sort(self):
        return 'opa, voce quer ordenar?'

lista = MyList()
print(lista.sort())
