from random import randint
listatupla = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print (f'Os valores são :{listatupla}')
numeroordem = (sorted(listatupla))
print(f'O menor número é: {numeroordem[0]}. E o maior número é: {numeroordem[-1]}')

#pode usar também o max(listatupla) e o min(listatupla) pra mostrar os numeros em ordem :)