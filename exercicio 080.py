num = list()
for c in range(0,5):
    n= (int(input('insira um valor aqui:')))
    if c ==0 or n > num[-1]:
        num.append(n)
        print('Foi adicionado no final da lista...')
    else:
        pos= 0
        while pos < len(num):
            if n<= num[pos]:
                num.insert(pos,n)
                print(f'Foi adicionado na posição {pos} da lista...')
                break
            pos+=1
print(f'Os valores digitados em ordem foram {num}')
