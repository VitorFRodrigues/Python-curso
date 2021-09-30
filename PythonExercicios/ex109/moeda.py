def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def metade(preco=0, show=False):
    if show:
        return moeda(preco/2)
    else:
        return preco/2


def dobro(preco=0, show=False):
    if show:
        return moeda(preco*2)
    else:
        return preco * 2


def aumentar(preco=0, perc=0, show=False):
    if show:
        return moeda(preco*(100+perc)/100)
    else:
        return preco * (100 + perc) / 100


def diminuir(preco=0, perc=0, show=False):
    if show:
        return moeda(preco*(100-perc)/100)
    else:
        return preco * (100 - perc) / 100

