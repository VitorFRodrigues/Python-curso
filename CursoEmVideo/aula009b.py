frase = 'Curso em Vídeo Python'
print(frase[::2])

# Imprimir Textos grandes
print(""" aaaaaaa
      bbbbbbb
      cccccccccc
      ddddddddddd""")

print(frase.upper().count('O'))
frase = '   Curso em Vídeo Python   '
print(len(frase.strip()))

print(frase.replace('Python', 'Android'))
print(frase)
frase = frase.replace('Python', 'Android')
print(frase)

dividido = frase.split()
print(dividido[0][3])