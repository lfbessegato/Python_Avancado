from operator import itemgetter
from itertools import groupby

linhas = [
	{'nome':'Marcos', 'data':'27/12/1987'},
	{'nome':'Joao', 'data':'18/11/1967'},
	{'nome':'Maria', 'data':'27/12/1987'},
	{'nome':'Julia', 'data':'18/11/1967'},
	{'nome':'Pedro', 'data':'18/11/1967'}
]

# ordena pelo campo data
linhas.sort(key=itemgetter('data'))

# faz a iteração
for data, items in groupby(linhas, key=itemgetter('data')):
	print(data)
	for i in items:
		print(' ', i)