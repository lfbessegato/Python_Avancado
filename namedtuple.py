from collections import namedtuple

Subcriber = namedtuple('Subscriber', ['id', 'email'])
sub = Subcriber('1000', 'marcos@live.com')

print(sub)
print(sub.id)
print(sub.email)

print(f'tamanho: {len(sub)}')
