from random import choice
al_1 = input('Digite o nome do aluno 1: ')
al_2 = input('Digite o nome do aluno 2: ')
al_3 = input('Digite o nome do aluno 3: ')
al_4 = input('Digite o nome do aluno 4: ')
lista = [al_1, al_2, al_3, al_4]
print('O aluno {} vai apagar o quadro.'.format(choice(lista)))