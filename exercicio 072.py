contagem = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove','dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dessesseis', 'dessesete', 'desoito', 'desenove', 'vinte'
while True:
    numero = int(input('Escreva o número desejado:'))
    if 0 <= numero <=20:
        break
    print('Número não contabilizado, tente novamente.', end= '')
print(f'O número escolhido foi {contagem[numero]}')
