while True:
    n = int(input('Digite um número para mostrar sua tabuada (Valor negativo para parar): '))
    if n < 0:
        break
    print('{:=^40}'.format(' TABUADA '))
    for c in range(1, 11):
        print(f'{n} x {c:2} = {c*n:2}')
    print('='*40)
print('Programa TABUADA encerrado. Volte Sempre!')