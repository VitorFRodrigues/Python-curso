from random import randint
from time import sleep

num = randint(0, 5)
print('-=-'*20)
num_user = int(input('Adivinhe o número que estou pensando.\nEle está entre 0 e 5: '))
print('-=-'*20)
print('Processando...')
sleep(3)
if num == num_user:
    print('Parabéns! Você venceu!')
else:
    print('Você errou! Eu pensei no número {}'.format(num))