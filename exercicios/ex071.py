print('MINHA RESOLUÇÃO')
cont = 1
from random import randint
print('-*-' * 40)
print('ESTOU PENSANDO EM UM NUMERO DE 0 A 10 ... TENTE ADVINHAR')
print('-*-' * 40)
c = randint(0, 10)
r = int(input('Em qual numero estou pensando ?'))
while r != c:
    if c > r:
        print('MAIS... tente novamente')
        r = int(input('Em qual numero estou pensando ?'))
        cont += 1
    else:
        print('MENOS...Tente novamente')
        r = int(input('Em qual numero estou pensando ?'))
        cont += 1
print('Parabens você acertou ! você tentou {} vezes e o numero que pensei foi {}'.format(cont, c) )

print('+-' * 40)
print('RESOLUÇÃO DO PROFESSOR')
print('+-' * 40)
from random import randint
comp = randint(0, 10)
print('Sou seu comptador... acabei de pensar em um numero entre 0 e 10')
print('Será que você consegue adivinhar qual foi ?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite ?'))
    palpites += 1
    if jogador == comp:
        acertou = True
    else:
        if jogador < comp:
            print('MAIS... Tente outra vez ')
        elif jogador > comp:
            print('MENOS... Tente outra vez')
print('PARABÉNS Você acertou com {} tentativas '.format(palpites))
