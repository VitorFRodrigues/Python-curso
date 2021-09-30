a = int(input('Digite um número aleatório: '))
b = int(input('Digite outro número aleatório: '))
c = int(input('Digite outro número aleatório: '))
#Verificando menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

#Verificando maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O número maior é {}'.format(maior))
print('O número menor é {}'.format(menor))

'''if n1 > n2:
    if n1 > n3:
        print('O número maior é {}'.format(n1))

if n2 > n1:
    if n2 > n3:
        print('O número maior é {}'.format(n2))

if n3 > n2:
    if n3 > n1:
        print('O número maior é {}'.format(n3))

if n1 < n2:
    if n1 < n3:
        print('O número menor é {}'.format(n1))

if n2 < n1:
    if n2 < n3:
        print('O número menor é {}'.format(n2))

if n3 < n2:
    if n3 < n1:
        print('O número menor é {}'.format(n3))'''