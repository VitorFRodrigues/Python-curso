from time import sleep


def contador(i, f, p):
    print('-=' * 20)
    if p == 0:
        p = 1
    p = abs(p)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        for c in range(i, f + 1, p):
            print(c, end=' ')
            sleep(.5)
        print('FIM!')
    else:
        for c in range(i, f - 1, -p):
            print(c, end=' ')
            sleep(.5)
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 30)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim:    '))
passo = int(input('Passo:  '))
contador(inicio, fim, passo)
