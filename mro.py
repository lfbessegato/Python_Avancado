class P():
    pass

p = P
print(P.__mro__)

class Veiculo():
    pass

class Carro(Veiculo):
    pass

class Trem(Veiculo):
    pass


class CarroTrem(Carro, Trem):
    pass

print(Veiculo.__mro__)
print(Carro.__mro__)
print(Trem.__mro__)

print(CarroTrem.__mro__)
