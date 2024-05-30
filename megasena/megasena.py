from random import randint
from time import sleep
print('-' * 40)
print('JOGA NA MEGA SENA')
print('-' * 40)
cont = contb = 0
j = int(input('Quantos jogos quer que eu sorteie ?'))
n = []
print( f'-=-=-= SORTEANDO OS {j} JOGOS -=-=-=')
while contb < j:
    for c in range(0, 6):
        p = (randint(0, 60))
        if p not in n:
            n.append(p)
        else:
            p = randint(0, 60)
            n.append(p)
    n.sort()
    print(f'Jogo {contb+1}: {n} ')
    contb += 1
    sleep(1)
    n.clear()
print('-=-' * 3, '< BOA SORTE! >', '-=-' * 3)
