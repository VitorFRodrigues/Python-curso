def leiaDinheiro(txt):
    valido = False
    while not valido:
        n = str(input(txt)).replace(',', '.').strip()
        if n.isalpha() or n == '':
            print(f'\033[0;31mERRO! \"{n}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(n)

