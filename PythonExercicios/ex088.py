from random import randint
from time import sleep
print('-'*30)
print('{:^30}'.format('JOGA NA MEGA SENA'))
print('-'*30)
n = int(input('Quantos jogos você deseja em sua cartela? '))
print('{:=^30}'.format(f'SORTEANDO {n} JOGOS'))
tabela = []
jogo = []
for c in range(0, n):
    cont = 0
    while cont < 6:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            cont += 1
    tabela.append(sorted(jogo[:]))
    jogo.clear()
for c in range(0, n):
    sleep(0.5)
    print(f'Jogo {c+1}: {tabela[c]}')
print('{:=^30}'.format(' BOA SORTE! '))
