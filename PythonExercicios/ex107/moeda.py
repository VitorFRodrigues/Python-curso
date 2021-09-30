def metade(preco):
    res = preco/2
    return res


def dobro(preco):
    res = preco*2
    return res


def aumentar(preco, perc=0):
    res = preco*(100+perc)/100
    return res


def diminuir(preco, perc=0):
    res = preco*(100-perc)/100
    return res

