n = int(input('Digite um número: '))
s = 0
for c in range(1, n+1):
    if n % c == 0:
        s += 1
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print(c, end=' ')
print('\033[m')
if s == 2:
    print('O número {} é primo.'.format(n))
else:
    print('O número {} não é primo.'.format(n))
