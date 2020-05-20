from collections import OrderedDict

# Ordered -> Mantém a Ordem
d = OrderedDict()
d['python'] = 10
d['java'] = 5
d['php'] = 6
d['C'] = 10

for key in d:
    print(key, d[key])
