from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
c = randint(0,2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
j = int(input('Escolha o que vai jogar:'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('POOOO')
print('-=' * 11)
print('Computador jogou {}'.format(itens[c]))
print('Jogador jogou {}'.format(itens[j]))
print('-=' * 11)
if c == 0:
    if j == 0:
        print('EMPATE')
    elif j == 1:
        print('JOGADOR VENCEU')
    elif j == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA')
elif c == 1:
    if j == 0:
        print('COMPUTADOR VENCEU')
    elif j == 1:
        print('EMPATE')
    elif j == 2:
        print('JOGADOR VENCEU')
elif c == 2:
    if j == 0:
        print('JOGADOR VENCEU')
    elif j == 1:
        print('COMPUTADOR VENCEU')
    elif j == 2:
        print('EMPATE')