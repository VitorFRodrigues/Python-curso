from time import sleep
c = ('\033[m',          # 0 - sem cores
     '\033[0;30;41m',   # 1 - vermelho
     '\033[0;30;42m',   # 2 - verde
     '\033[0;30;43m',   # 3 - amarelo
     '\033[0;30;44m',   # 4 - azul
     '\033[0;30;45m',   # 5 - roxo
     '\033[7;30m',      # 6 - branco
     )


def escreva(txt, cor=0):
    tamanho = len(txt) + 4
    print(c[cor], end='')
    print('~' * tamanho)
    print(f'  {txt}  ')
    print('~' * tamanho)
    print(c[0], end='')
    sleep(2)


def ajuda(comando):
    escreva(f'Acessando o manual do \'{dado}\'', 4)
    print(c[6], end='')
    help(comando)
    print(c[0], end='')
    sleep(1)


while True:
    escreva('SISTEMA DE AJUDA PyHELP', 2)
    dado = str(input('Função ou Biblioteca > '))
    if dado.lower() == 'fim':
        break
    else:
        ajuda(dado)
escreva('ATÉ LOGO!', 1)
