resp = 'S'
num = list()
while 'S' in resp:
    num.append(input('Escreva um número:'))
    resp = str(input('Vcoê deseja continuar colocando números?').strip().upper())
print(num)