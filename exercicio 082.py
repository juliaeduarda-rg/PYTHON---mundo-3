num = list()
par = list()
impar = list()
r = 'S'
while True:
    n = int(input('Escreva um número:'))
    num.append(n)
    if n % 2 == 0:
        par.append(n)
    elif n % 2 != 0:
        impar.append(n)
    r = str(input('Deseja continuar? SxN').strip().upper())
    if r == 'N':
        break
print(f'A lista de todos os números são {num}')
print(f'A lista dos números par são {par}')
print(f'A lista dos números ímpar são {impar}')
