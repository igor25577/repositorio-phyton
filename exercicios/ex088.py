time = ('Atlético - MG', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Bragantino', 'Corinthians', 'Fluminense', 'Cuiabá',
'Internacional','Atlético - GO', 'Athletico-Pr', 'Ceará', 'Santos', 'Juventude', 'Bahia', 'São Paulo', 'América - MG',
'Grêmio', 'Sport', 'Chapecoense')
ordem = sorted(time)
print(time)
print('-=-' * 40)
print(f'Os cinco primeiros colocados da tabela são : {(time[0:5])}')
print('-=-' * 40)
print(f'Os quatro ultimos são : {(time[-4:])}')
print('-=-' * 40)
print(f'Os times em ordem alfabetica : {ordem}')
print('-=-' * 40)
print(f'O Chapecoense está na {time.index("Chapecoense")+1}ª posição')
print('-=-' * 40)