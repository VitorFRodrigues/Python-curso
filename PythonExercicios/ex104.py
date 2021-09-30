def leiaInt(txt):
    n = input(txt)
    while n.isnumeric() is False:
        print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        n = input(txt)
    return n


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
