from random import randint
from time import sleep
print('{:=^40}'.format('JOKENPÔ'))
print('Pedra, Papel e Tesoura')
user = str(input('Bem vindo ao jogo!\nDigite Pedra, Papel ou Tesoura: ')).upper().strip()
lista = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ!!!')

if user in lista:

    print('-='*11)
    print('Computador: {}\nUser: {}'.format(lista[computador], user))
    print('-='*11)

    if user == lista[computador]:
        print('Deu empate, eu escolhi {} e você escolheu {}.'.format(lista[computador], user))

    if user == 'PEDRA':
        if lista[computador] == 'PAPEL':
            print('Eu ganhei! Escolhi {} e você {}.'.format(lista[computador], user))
        elif lista[computador] == 'TESOURA':
            print('Você venceu! Escolhi {} e você {}.'.format(lista[computador], user))
    elif user == 'PAPEL':
        if lista[computador] == 'TESOURA':
            print('Eu ganhei! Escolhi {} e você {}.'.format(lista[computador], user))
        elif lista[computador] == 'PEDRA':
            print('Você venceu! Escolhi {} e você {}.'.format(lista[computador], user))
    elif user == 'TESOURA':
        if lista[computador] == 'PEDRA':
            print('Eu ganhei! Escolhi {} e você {}.'.format(lista[computador], user))
        elif lista[computador] == 'PAPEL':
            print('Você venceu! Escolhi {} e você {}.'.format(lista[computador], user))
else:
    print('JOGADA INVÁLIDA!')