
class Objeto:
    def __init__(self, obj_id):
        self.obj_id = obj_id
    
    def __repr__(self):
        return str(self.obj_id)

objetos = [Objeto(90), Objeto(15), Objeto(20)]

print(objetos)

print (f'Ordenacao: {sorted(objetos, key=lambda obj: obj.obj_id)}')