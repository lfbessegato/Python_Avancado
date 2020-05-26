texto1 = '             python             '
print(texto1)
print(f'Removendo os espaco em branco inicio/fim: {texto1.strip()}')

texto2= '---------python----------'
print(texto2)
print(f'Removendo caracacteres do inicio/fim: ', {texto2.strip('-')})

texto3 = '             python'
print(texto3)
print(f'Removendo os espaco em branco da esquerda: {texto3.lstrip()}')

texto4= 'python      '
print(texto4)
print(f'Removendo caracacteres da direita: ', {texto4.rstrip()})