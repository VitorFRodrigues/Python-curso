def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def metade(preco, show=False):
    if show:
        return moeda(preco/2)
    else:
        return preco/2


def dobro(preco, show=False):
    if show:
        return moeda(preco*2)
    else:
        return preco * 2


def aumentar(preco, perc=0, show=False):
    if show:
        return moeda(preco*(100+perc)/100)
    else:
        return preco * (100 + perc) / 100


def diminuir(preco, perc=0, show=False):
    if show:
        return moeda(preco*(100-perc)/100)
    else:
        return preco * (100 - perc) / 100


def escreva(txt):
    tamanho = len(txt) + 16
    print('-'*tamanho)
    print(f'        {txt}')
    print('-'*tamanho)


def resumo(preco, aum, dim):
    escreva('RESUMO DO VALOR')
    print(f'{"Preço analisado:":<20}{moeda(preco)}\n'
          f'{"Dobro do preço:":<20}{dobro(preco, True)}\n'
          f'{"Metade do preço:":<20}{metade(preco, True)}\n'
          f'{aum}{"% de aumento:":<18}{aumentar(preco, aum, True)}\n'
          f'{dim}{"% de aumento:":<18}{diminuir(preco, dim, True)}\n')

