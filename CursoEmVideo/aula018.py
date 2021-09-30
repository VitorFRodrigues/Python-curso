#LISTAS COMPOSTAS
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])
print('-='*30)

teste = []
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(teste)
print(galera)
print('-='*30)

galera2 = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera2:
    print(f'{p[0]} tem {p[1]} anos de idade.')
print('-='*30)

galera3 = []
dado = []
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(str(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

print(galera3)
for p in galera3:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')
