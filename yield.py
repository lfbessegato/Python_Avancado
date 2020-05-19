# yield - retorna um generator (objeto)
# Yield no Python é usado sempre que você precisa definir uma função de gerador de algo. 
# Você não pode usar yield fora de um generator function. Quando você usa a instrução yield dentro de uma função, 
# ela se transforma em uma função geradora. ... O yield retém o estado da função onde ela é pausada 
# (ao retornar o value ).

'''
Ele retorna um valor mantendo o estado de onde parou. Quando executa de novo ele continua de onde parou. 
Ele controla o estado de um enumerador entre execuções da função.
'''

def gerador():
    for i in range(5):
        yield i

g = gerador()
print(g)
print(next(g))