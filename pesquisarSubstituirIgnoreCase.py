import re
texto = 'JAVA, java, Java'

print(texto)
print(re.sub('java', 'python', texto, flags=re.IGNORECASE))