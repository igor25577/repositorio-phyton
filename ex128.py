from utilitarios import moeda

p = float(input('Digite o preço R$:'))
print(f'A metade de {moeda.moedas(p)} é {moeda.moedas(moeda.metade(p))}')
print(f'O dobro de {moeda.moedas(p)} é {moeda.moedas(moeda.dobro(p))}')
print(f'Aumentado 10% temos {moeda.moedas(moeda.aumento(p, 10))} ')
print(f'Reduzindo 13% temos {moeda.moedas(moeda.redutor(p, 13))} ')
