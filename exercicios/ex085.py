from random import randint
print('$' * 40)
print('{:^40}'.format('BEM VINDO AO ARAUJO´S BANK'))
print('$' * 40)
valor = int(input('Quanto deseja sacar ? R$:'))
tot = valor
ced = 50
totced = 0
while True:
    if tot >= ced:
        tot -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Foram {totced} cedulas de R${ced:.2f}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if tot == 0:
            break