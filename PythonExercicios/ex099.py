from time import sleep


def maior(* num):
    maior = 0
    print('-='*30)
    print('Analisando os valores passados...')
    if len(num) > 0:
        for i, c in enumerate(num):
            print(c, end=' ')
            if i == 0:
                maior = c
            else:
                if c > maior:
                    maior = c
            sleep(.2)
        print(f'Foram {len(num)} valores ao todo.\n'
              f'O maior valor informado foi {maior}.')
    else:
        print('Foram informados 0 valores ao todo.\n'
              'O maior valor informado foi 0.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
