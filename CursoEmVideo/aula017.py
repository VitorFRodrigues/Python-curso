lanche = ['hamburguer', 'suco', 'pizza', 'pudim'] #lista
lanche[3] = 'picolé' #Substitui o indice 3 de lanche (pizza) por picolé
lanche.append('coockie') #add cookie no indice 4
lanche.insert(0, 'cachorro-quente') #insere cachorro-quente na posição 0 e 'empurra' o restante para frente
del lanche[3] # deleta indice 3 de lanche e rearranja
lanche.pop(3) # deleta indice 3 de lanche e rearranja
lanche.pop() # remove o objeto da ultima casa
if 'pizza' in lanche:
    lanche.remove('pizza') #remove a variavel pizza da lista se ela estiver no local ele vai buscar no
                            # inicio da lista até o proximo. Se houver duas 'pizza'

valores = list(range(4, 11)) #cria lista de valores de 4 a 10

valores = list(range(4, 11, 2)) #cria lista de valores de 4 a 10 pulando de 2 em 2

valores = [8, 2, 5, 4, 9, 3, 0]

valores.sort() #ordena todos os valores
valores.sort(reverse=True) #ordena os valores de forma invertida

len(valores) #diz a quantidade de elementos da lista

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
num.sort(reverse=True)
num.insert(2, 0)
num.pop()
num.pop(2)
num.remove(2)
print(num)
print(f'Essa lista tem {len(num)} elementos.')

valores = [] # vc tbm pode escrever valores = list() dá no mesmo
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

a = [2, 3, 4, 7]
b = a #Linka b com a, ou seja, se eu mudar algo em b, a tbm vai mudar
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista A: {b}')

a = [2, 3, 4, 7]
b = a[:] #faz uma cópia de a em b, agora posso modificar b sem modificar a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista A: {b}')

