#Tuplas
#AS TUPLAS SÃO IMUTÁVEIS!
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'
print(lanche)
print(lanche[1])
print(lanche[3])
print(lanche[-2])
print(lanche[1:3]) #desconsidera o ultimo
print(lanche[2:])
print(lanche[:2])
print(lanche[-3:])
print(len(lanche))
#lanche[1] = 'Refrigerante' COMANDO ERRADO! TUPLAS SÃO IMUTAVEIS

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi pra caramba!')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')

print(sorted(lanche)) #mostra a tupla ordenada alfabeticamente
print(lanche)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(len(c))
print(c.count(5))
print(c.index(5, 1)) #Busque o indexador de 5 e procure a partir da posição 1

pessoa = ('Gustavo', 39, 'M', 99.88) #pode haver tipos diferentes de dados
del(pessoa) #apagar a tupla inteira da memoria
