from random import randint
cont = 0
while True:
    print('{:=^40}'.format(' PAR OU IMPAR '))
    escolha = str(input('Par ou Impar? ')).strip().upper()[0]
    while escolha not in 'PI':
        escolha = str(input('Par ou Impar? ')).strip().upper()[0]
    user = int(input('Digite seu número (0 a 5): '))
    computador = randint(0, 5)
    resposta = user + computador
    if escolha == 'P':
        print(f'Escolha: PAR\n'
              f'Usuário: {user}\n'
              f'Computador: {computador}\n'
              f'Resposta: {resposta}')
        if resposta % 2 == 0:
            print('Parabéns! Voce ganhou!')
            cont += 1
        else:
            break
    elif escolha == 'I':
        print(f'Escolha: IMPAR\n'
              f'Usuário: {user}\n'
              f'Computador: {computador}\n'
              f'Resposta: {resposta}')
        if resposta % 2 == 0:
            break
        else:
            print('Parabéns! Voce ganhou!')
            cont += 1
    print('Vamos Jogar novamente...')
print(f'GAME OVER! '
      f'Você me venceu {cont} vezes.')