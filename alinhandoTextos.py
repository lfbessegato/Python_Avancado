textos = 'Apredendo Python'
print(textos, '---', 'Alinhando a esquerda: ', {textos.ljust(20)})
print(textos, '---', 'Alinhando a direita: ', {textos.rjust(20)})
print(textos, '---', 'Alinhando centro: ', {textos.center(20)})

#Exemplo com o format
print(textos, '---', 'Alinhando a esquerda com o format: ', format(textos, '->20s'))
print(textos, '---', 'Alinhando a direita com o format: ', format(textos, '-<20s'))
print(textos, '---', 'Alinhando centro com o format: ', format(textos, '-^20s'))