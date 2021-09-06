num = list()
r = 'S'
cont= 0
while r == 'S':
    n = int(input('Escreva um número'))
    num.append(n)
    cont += 1
    r = str(input('Deseja continuar escrevendo? [SxN]').strip().upper())
print(f'Você digitou {cont} números')
num.sort(reverse= True)
print(f'Os valores em ordem decrescente são {num}')
if 5 in num:
    print('O número 5 foi digitado!')
else:
    print('O número 5 não foi digitado!')