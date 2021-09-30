a = float(input('Digite o lado A do triângulo: '))
b = float(input('Digite o lado B do triângulo: '))
c = float(input('Digite o lado C do triângulo: '))

if (abs(b-c) < a) and (a < b+c) and (abs(a-c) < b) and (b < a+c) and (abs(a-b) < c) and (c < a+b):
    print('Pode formar um triângulo ', end='')
    if a == b == c:
        print('Equilátero.')
    elif a != b != c != a:
        print('Escaleno.')
    else:
        print('Isósceles.')
else:
    print('Este triângulo não é possível.')