menu = 0
a = int(input('Digite o 1° valor: '))
b = int(input('Digite o 2° valor: '))

while menu != 5:
    print('{:=^16}'.format('MENU'))
    print('[1] somar\n'
          '[2] multiplicar\n'
          '[3] maior\n'
          '[4] novos números\n'
          '[5] sair do programa')
    print('='*16)
    menu = int(input('O que deseja fazer? '))
    if menu == 1:
        soma = a + b
        print('{} + {} = {}'.format(a, b, soma))
    elif menu == 2:
        multiplicacao = a * b
        print('{} * {} = {}'.format(a, b, multiplicacao))
    elif menu == 3:
        if a > b:
            print('O maior valor é {}'.format(a))
        elif a == b:
            print('Os valores são iguais.')
        else:
            print('O maior valor é {}'.format(b))
    elif menu == 4:
        a = int(input('Digite o 1° valor: '))
        b = int(input('Digite o 2° valor: '))
    elif menu == 5:
        print('PROGRAMA FINALIZADO!')
    else:
        print('Opção inválida. Tente novamente.')
