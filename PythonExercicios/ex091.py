from random import randint
from time import sleep
from operator import itemgetter
sorteio = {}
ranking = []
sorteio['jogador1'] = randint(1, 6)
sorteio['jogador2'] = randint(1, 6)
sorteio['jogador3'] = randint(1, 6)
sorteio['jogador4'] = randint(1, 6)
print('Valores sorteados:')
for k, v in sorteio.items():
    print(f'    O {k} tirou {v}.')
    sleep(.5)

ranking = sorted(sorteio.items(), key=itemgetter(1), reverse=True) #põe sorteio em ordem. Se quiser ordem de Key itemgetter(0) se quiser ordem de value itemgetter(1)
print('Raking dos jogadores:')

for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}')
    sleep(.5)
