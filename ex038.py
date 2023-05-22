import random
from time import sleep
v = random.randint(70,120)
print('Na rodovia 106 as 10:46Am o seu carro passou em um radar à {}Km/h'.format(v))
sleep(2)
if v > 80:
    print('E você foi multado!')
    print('E por passar à {}Km/h, sua multa será {:.2f}R$'.format(v,(v-80)*7))
else:
    print('Parabens por dirigir com segurança e no limite continue assim!')
