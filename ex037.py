import random
from time import sleep
print('-=-'*30)
print('Estou pensando em um numero de 0 a 5 tente advinhar')
print('-=-'*30)
NE = int(input('Digite o numero que acha que é:'))
print('PROCESSANDO...')
sleep(3)
NP = random.randint(0, 5)
if NE == NP:
    print('Parabéns você acertou!')
else:
    print('Errado! tente outra vez!')
    print('Eu pensei no numero {} e não no {}'.format(NP, NE))
