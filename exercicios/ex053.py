r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar um triângulo')
    if r1==r2 and r2==r3:
        print('O triângulo formado é um EQUILÁTERO')
    elif r1==r2 or r1==r3 or r2==r1 or r2==r3 or r3==r1 or r3==r2:
        print('O triângulo formado é um ISÓSCELES')
    else:
        print('O triângulo formado é um ESCALENO')
else:
    print('Os segmentos não podem formar um triângulo ')



