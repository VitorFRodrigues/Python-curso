help(print) #mostra na tela a funcionalidade de print

print(print.__doc__) #mostra mais informações de print em formatação diferente


def contador(i, f, p):
    """
    ->Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Gustavo Guanabara do canal CursoemVideo
    """                                                     #DOCSTRING: Explica a função para quem queira digitar o help terá uma explicação
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


contador(2, 10, 2)
help(contador)

def somar(a,b,c=0): #PARAMETRO OPCIONAL: o c=0 indica que se na chamada da função eu não informar a terceira variavel, c será igual a zero
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(8, 4)


def teste():
    global n #N dentro da função passa a ser global
    x = 8 #variável local
    n = 10 # variavel global
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


#Programa principal
n = 2 #variável global
print(f'No programa principal, n vale {n}')
teste()
print(f'No programa principal, x vale {x}')


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


print(somar(3, 2, 5))
resp = somar(3, 2, 5)


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')
