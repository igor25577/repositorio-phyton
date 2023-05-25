dados = {}
listag = []
tot = 0
dados['Nome'] = str(input('Digite o nome de um jogador: '))
partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou ?'))
for p in range(0, partidas):
    gols = int(input(f'Quantos gols ele fez na {p+1}º partida ?'))
    listag.append(gols)
    dados['gols'] = listag[:]
    tot += gols
    dados['totgol'] = tot
print('-=-' * 20)
print(dados)
print('-=-' * 20)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v} ')
print('-=-' * 20)
print(f'O jogador {dados["Nome"]} Jogou {partidas} partidas')
for c in range(0, partidas):
    print(f'  => Na {c+1}º partida, fez {listag[c]} gols.')
print(f'Foram marcados {dados["totgol"]} gols no total')
