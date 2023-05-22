from utilitarios import moeda

p = float(input('Digite o preço R$:'))
print(f'A metade de {moeda.moedas(p)} é {moeda.metade(p,True)}')
print(f'O dobro de {moeda.moedas(p)} é {moeda.dobro(p,True)}')
print(f'Aumentado 10% temos {moeda.aumento(p, 10, True)} ')
print(f'Reduzindo 13% temos {moeda.redutor(p, 13, True)} ')
