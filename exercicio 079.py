resp = 'S'
num = list()
while 'S' in resp:
    num.append(input('Escreva um número:'))
    num.append(n)
    elif n in num:
        print('Já existe esse número aqui, porfavor escreva outro número')
    resp = str(input('Vcoê deseja continuar colocando números?').strip().upper())
num.sort()
print(f'Os números escritos em ordem crescente foram:{num}')
