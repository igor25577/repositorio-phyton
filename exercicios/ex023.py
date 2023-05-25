import math
ângulo=float(input('digite o ângulo que deseja:'))
seno1=math.sin(math.radians(ângulo))
print('O ângulo de:{}º tem o seno de:{:.2f}'.format(ângulo,seno1))
cosseno1=math.cos(math.radians(ângulo))
print('o ângulo de:{}º tem o cosseno de:{:.2f}'.format(ângulo,cosseno1))
tangente1=math.tan(math.radians(ângulo))
print('o ângulo de:{}º tem a tangente de :{:.2f}'.format(ângulo,tangente1))

print('ou:')

from math import radians,sin,cos,tan
ângulo=float(input('digite o ângulo que deseja:'))
seno2=sin(radians(ângulo))
print('o Ângulo de:{}º tem o seno de:{:.2f}'.format(ângulo,seno2))
cosseno2=cos(radians(ângulo))
print('o ângulo de:{}º tem o cosseno de:{:.2f}'.format(ângulo,cosseno2))
tangente2=tan(radians(ângulo))
print('o ângulo de:{}º tem o cosseno de:{:.2f}'.format(ângulo,tangente2))