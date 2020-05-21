from collections import Counter

# Counter -> Contabilizar dados.


a = Counter([1,1,2,2,3,4,4,5,6])
b = Counter([2,2,1,3,5,6,7])

print(f'Sequencia a: {a}')
print(f'Sequencia b: {b}')

# Juntando as duas sequencias
print(f'Juntando as duas sequencias: {a+b}')