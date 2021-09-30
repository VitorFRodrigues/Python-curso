def leiaInt(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não informar esse número!\033[m')
            return 0
        else:
            return n


def leiaFloat(txt):
    while True:
        try:
            n = float(input(txt))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não informar esse número!\033[m')
            return 0
        else:
            return n


i = leiaInt('Digite um Inteiro: ')
r = leiaFloat('Digite um Real: ')
print(f'O valor ineiro digitado foi {i} e o real foi {r}')
