from random import randint
from operator import itemgetter
from time import sleep
res = {}
ranking = []
for c in range(0, 4):
    n = randint(0, 6)
    print(f'O {c+1}ª jogador jogou o dado e caiu no {n}')
    sleep(1)
    res[f"Jogador{c+1}"] = n
    res.copy()
ranking = sorted(res.items(), key=itemgetter(1), reverse=True)
print('-=-' * 10)
print('      ===== RANKING DOS JOGADORES =====')
for i, v in enumerate(ranking):
    print(f'Em {i+1}º lugar ficou o {v[0]} que tirou {v[1]}')
    sleep(1)
