times = 'Fortaleza EC', 'Athletico-PR', 'Atlético Goianiense', 'Bragantino', 'Bahia', 'Fluminense', 'Palmeiras', 'Flamengo', 'Atlético-MG', 'Corinthians', 'Ceará', 'Santos', 'Cuiabá','Sport', 'São Paulo', 'Juventude', 'Internacional', 'Grêmio', 'América-MG', 'Chapecoense'
print(f'Os 5 primeiros colocados são: {times [0:5]}')
print(f'Os ultimos 4 colocados são: {times [16:]}')
print(sorted(times))
print(f'O time Chapecoense está em {times.index("Chapecoense") +1}º posição')