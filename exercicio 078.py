listatop = []
for i in range(0,5):
    listatop.append(int(input('Escreva um número:')))
print(f'Seu maior número foi {max(listatop)} ')
print(f'Seu menor número foi {min(listatop)} ')
mx = max(listatop)
mn= min(listatop)
print('O meior número está na posição ', end=' ')
for c, v in enumerate(listatop):
    if v == mx:
        print(f'{c+1}', end=' ')
print(' ')
print('O menor número está na posição ', end= ' ')
for c, v in enumerate(listatop):
    if v == mn:
        print(f'{c+1}', end=' ')
