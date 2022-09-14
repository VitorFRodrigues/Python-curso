# > LISTAS

# Antes
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# Com lista
notas = [7.9, 9.7, 8.2]

# Criando Listas
lista = []
lista = list()
lista = [26, 'Vitor', 3.14159, False]
lista_de_listas = [10, [1, 2, 3]]

# Indexação e Slices (fatiamento)

lista = [26, 'Vitor', 3.14159, False]
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

print(lista[-1])

# Slices

lista = [10, 50, 30, 40, 25, 60, 5]

print(lista[0:3])
print(lista[3:6])
print(lista[3:])
print(lista[2:6:2])

# > Interações com FOR

# 1. Utilizando os próprios elementos da lista

for elemento in lista:
    print(elemento)

# 2. Utilizando os índices

print(f'Comprimento da lista: {len(lista)}')
for i in range(len(lista)):
    print(lista[i])

# > MÉTODOS DE LISTAS
lista = [1, 3, 12, 8, 2]
# append

print(f'Antes do append: {lista}')
lista.append(3)
print(f'Depois do append: {lista}')

# insert
lista.insert(2, 10)
print(f'Depois do insert: {lista}')

# extend
lista2 = [1, 2, 3]
lista.extend(lista2)
print(f'Depois do extend: {lista}')

# pop
lista.pop()
print(f'Depois do pop: {lista}')

lista.pop(0)
print(f'Depois do pop: {lista}')

# remove
lista.remove(3)
print(f'Depois do remove: {lista}')

# count
print(f'Quantidade de 2 na lista: {lista.count(2)}')

# index
print(f'Índice do elemento 12: {lista.index(12)}')

# sort
print(f'Lista em ordem crescente: {lista.sort()}')
print(f'Lista em ordem decrescente: {lista.sort(reverse=True)}')

# FUNÇÕES PARA LISTAS

# len
print(len(lista))

# sum
print(sum(lista))

# Maior elemento da lista
print(max(lista))

# Menor elemento da lista
print(min(lista))