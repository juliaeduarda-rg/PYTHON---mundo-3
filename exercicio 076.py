livros = ('O conto de aia', 18.00, 'O homem de giz', 30.00,'Fahrenheit 451', 20.00, 'O morro dos ventos uivantes', 12.00,
          'Box de Sherlock Holmes', 72.00, 'Box jane Austin',  55.00,'A menina que roubava livros', 12.00,
          'Todo esse tempo', 24.00)
print('='*42)
print(f'{"LISTA DE LIVROS":^40}')
print('='*42)
for repeticao in range(0,len(livros)):
    if repeticao % 2 == 0:
        print(f'{livros[repeticao]:.<34}', end= '')
    else:
        print(f'R$ {livros[repeticao]:.2f}')