frase = 'Curso em Video Python' #Cadeia de caracteres, cada digito é numerado de 0 até o ultimo dígito

print(frase[9]) #imprime o digito da casa 9 (lembrando q a contagem das casas se inicia em 0)
print(frase[9:13]) #imprime os digitos da casa 9 até a casa 12 (no python, a ultima casa é suprimida)
print(frase[9:21]) #imprime os digitos da casa 9 até a casa 20 (ultimo digito da frase)
print(frase[9:21:2]) #imprime os digitos da casa 9 até a casa 20 pulando de 2 em 2
print(frase[:5]) #imprime os digitos iniciais até a casa 4
print(frase[15:]) #imprime os digitos a partir da casa 15 até o final
print(frase[9::3]) #imprime os digitos a partir da casa 9 até o final pulando de 3 em 3
len(frase) #Informa o comprimento da frase (nesse caso 21)
frase.count('o') #Conta o número de 'o' na frase
frase.count('o', 0, 13) #Conta o número de 'o' na frase do inicio a casa 12
frase.find('deo') #Informa a casa em que inicia 'deo', vai ser informado a posição do 'd'
frase.find('Android') #Se a função buscar na frase e não encontrar o solicitado, será retornado o valor -1
'Curso' in frase #'Existe a palavra dentro de frase?' Será retornado o valor True ou False
frase.replace('Python', 'Android') #busca a palavra e substitue pela seguinte (não precisa ter mesmo tamanho)
frase.upper() #Transforma tudo em maiúsculo
frase.lower() #Transforma tudo em minusculo
frase.capitalize() #Transforma tudo em minusculo e poe apenas a primeira letra da primeira palavra em maiúsculo
frase.title() #Transforma tudo em minusculo e poe a primeira letra de cada palavra em maiúsculo

frase = '   Aprenda Python  '
frase.strip() #Retira espaços desnecessários no inicio e no fim da frase. A letra 'A' fica na casa 0. (NÃO RETIRA ESPAÇOS DO MEIO)
frase.rstrip() #Retira espaços desnecessários da direita da frase. (NÃO RETIRA ESPAÇOS DO MEIO)
frase.lstrip() #Retira espaços desnecessários da esquerda da frase. (NÃO RETIRA ESPAÇOS DO MEIO)

frase = 'Curso em Video Python' #Cadeia de caracteres, cada digito é numerado de 0 até o ultimo dígito
frase.split() #divide a frase em palavras e as poe dentro de uma lista. Cada palavra recebe identificaçao nova de 0 até o tamanho dela
'-'.join(frase) #Uni as palavras da frase usando '-' ao inves de espaço 'Curso-em-Video-Python'