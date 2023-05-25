print('$$$' * 40)
print('BEM-VINDO A LOJAS ARAUJO!')
print('$$$' * 40)
tot = produtc = menor = cont = 0
barato = ' '
while True:
    p = str(input('Digite o nome do produto que deseja passar:')).strip()
    pp = float(input('Qual o preço do produto:R$'))
    r = ' '
    cont += 1
    tot += pp
    while r not in 'SN':
        r = str(input('Deseja continuar ?[S/N]')).strip().upper()[0]
    if r == 'N':
        break
    if cont == 1:
        barato = p
        menor = pp
    else:
        if pp < menor:
            menor = pp
            barato = p
    if pp >= 1000:
        produtc += 1
    if r == 'N':
        break
print(f'O total gasto foi R${tot:.2f}, Você comprou {produtc} produtos acima de R$1000')
print(f'O produto mais barato da lista foi : {barato}')