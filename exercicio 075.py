tuplanumero = (int(input('Escreva um número:')),int(input('Escreva um número:')),
               int(input('Escreva um número:')),int(input('Escreva um número:')),int(input('Escreva um número:')))
print(f'você escreveu os números {tuplanumero} ')
print(f'O valor 9 apareceu {tuplanumero.count(9)} vezes')
if 3 in tuplanumero:
    print(f'o primeiro valor 3 apareceu em {tuplanumero.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em lugar nenhum.')
print(f'Os valores pares digitados foram ', end= '')
for n in tuplanumero:
    if n % 2 == 0:
        print(n, end=' ')
