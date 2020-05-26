texto = 'java eh legal, java eh uma linguagem rapida'
print(texto)

print(texto.replace('java', 'python'))

import re
texto = 'a data de meu aniversario eh 26/01/1971'
print(re.sub(r'(\d+)/(\d+)/(\d+)',r'\3-\1-\2',texto))

# Exemplo utilizando o compile
pat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(re.sub(pat, r'\3-\2-\1',texto))