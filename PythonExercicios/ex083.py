abre = fecha = 0
n = str(input('Digite a expressão: ')).strip()
for parenteses in n:
    if '(' in parenteses:
        abre += 1
    elif ')' in parenteses:
        fecha += 1
if abre == fecha:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
