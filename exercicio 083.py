exp = str(input('Escreva uma expressão númerica:'))
abre = (exp.count('('))
fecha = (exp.count(')'))
if abre == fecha:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')