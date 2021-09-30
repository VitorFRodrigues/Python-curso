n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2

if media >=7:
    print('A sua media foi {:.2f}. Parabens! Você Passou!'.format(media))
else:
    print('A sua media foi {:.2f}. Você reprovou! Mais sorte na próxima vez.'.format(media))

'''nome = str(input('Qual é o seu nome? '))
if nome == 'Vitor':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))'''