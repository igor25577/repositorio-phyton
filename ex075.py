print('<x.x>' * 40)
print('GERADOR DE PA')
print('<x.x>' * 40)
num = int(input('Digite o primeiro termo :'))
r = int(input('Digite a razão da PA :'))
termo = num
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -->'.format(termo), end='')
        termo += r
        cont += 1
    print('PAUSA...')
    mais = int(input('Quantos termos a mais deseja ver ?'))
print('foram exibidos {} termos'.format(total))
print('FINALIZANDO O PROGRAMA ...')