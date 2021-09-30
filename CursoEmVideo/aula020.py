def soma(a, b):
    print(f'{a}+{b}={a+b}')
def contador(*num):
    print(f'Numeros:{num}\n'
          f'Contador: {len(num)}')
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(lst)


#Programa Principal
soma(4, 5)
soma(a=8, b=9) #pode mostrar dessa maneira
soma(b=2, a=1) #pode inverter se quiser

contador(2, 1, 5)
valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)