frase = str(input('Digite uma frase: ')).strip().lower()
print('A letra "A" aparece {} vezes'.format(frase.count('a')))
print('A letra primeira letra "A" aparece na posição {} da frase'.format(frase.find('a')))
print('A letra ultima letra "A" aparece na posição {} da frase'.format(frase.rfind('a')))
