print('{:=^40}'.format(' Sequência Fibonacci '))
n = int(input('Digite a quantidade de digitos da sequencia: '))

fib_1 = 0
fib_2 = 1
print('{} -> {} ->'.format(fib_1, fib_2), end=' ')
fib_3 = fib_1 + fib_2
n -= 2
while n > 0:
    print(fib_3, end=' -> ')
    fib_1 = fib_2
    fib_2 = fib_3
    fib_3 = fib_1 + fib_2
    n -= 1
print('ACABOU!')