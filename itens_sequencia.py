from collections import Counter

palavras = ['marcos', 'joao', 'felipe', 'marcos', 'carol', 'joao', 'marcos', 'maria', 'joao', 'felipe']
print(f'Palavras= {palavras}')

palavras_cont = Counter(palavras)

# Duas palavras mais comuns
print(f'Duas palavras mais comuns: {palavras_cont.most_common(2)}')

# Três palavras mais comuns
print(f'Tres palavras mais comuns: {palavras_cont.most_common(3)}')