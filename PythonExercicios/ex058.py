'''from random import randint
usuario = -1
tentativa = 0
computador = randint(0, 10)

while computador != usuario:
    usuario = int(input('Adivinhe o número que estou pensando.\nEle está entre 0 e 10: '))
    tentativa += 1
    if computador > usuario:
        print('Mais... Tente mais uma vez')
    elif computador < usuario:
        print('Menos... Tente mais uma vez.')


print('PARABÉNS! VOCÊ VENCEU!\nForam necessárias {} tentativas para você me vencer.'.format(tentativa))'''
from random import randint
computador = randint(0, 10)
print('Sou o seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))