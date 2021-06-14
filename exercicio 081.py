resp = 'S'
num = list()
num2 = list()
while 'S' in resp:
    num.append(int(input('Escreva um número:')))
    while :
        resp = str(input('Você deseja continuar colocando números?').strip().upper())
print(f'{len(num)} números foram digitados.')
num.sort(reverse=True)
print(f'Os números digitados em ordem decrescente são:', end='')
for c in range(len(num)):
    print(num[c], end='')
if num in 5:
   print(f'\nO número 5 está na lista. Na posição {num2.index(5)}')
else:
   print('O número 5 não está na lista.')