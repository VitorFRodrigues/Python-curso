frase = str(input('Digite uma frase: ')).strip().upper()
quebra = frase.split()
junta = ''.join(quebra)
'''junta_inv = ''
for c in range(len(junta)-1, -1, -1):
    junta_inv += junta[c]'''
junta_inv = junta[::-1]

if junta == junta_inv:
    print('Esta frase é um palíndromo!\n'
          'Ela normal é {}\n'
          'Ela invertida é {}'.format(junta, junta_inv))
else:
    print('Esta frase não é um palíndromo!\n'
          'Ela normal é {}\n'
          'Ela invertida é {}'.format(junta, junta_inv))