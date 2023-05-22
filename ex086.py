lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-3:])

for comida in lanche:
    print(f'Eu vou comer {comida}')

print(len(lanche))

for cont in range(0, len(lanche)):
    print(f'Eu vou comer{lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição{pos}')

print('EU COMI PRA CARAMBA')

print(sorted(lanche))

a = (5, 7, 8, 2)
b = (4, 8, 7, 3)
c = a + b
print(c)