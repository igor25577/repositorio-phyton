print('-=-' * 40)
print('BEM-VINDO AO ARMAZENS CEARA')
print('-=-' * 40)
produtos = ('lapis', '1.00', 'caneta', '2.00', 'caderno', '18.50', 'fichario', '32.50', 'fichario', '87.50',
            'mochila', '55.90', 'mochila', '109.99')

for pos in range(0,len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}',end='')
    else:
        print('R$:'f'{produtos[pos]:>7}')
print('-=-' * 40)
print('FIM DA LISTA...')