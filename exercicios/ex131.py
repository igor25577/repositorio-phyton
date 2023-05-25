from utilitarios import moeda
from utilitarios import dados

p = dados.leiaDinheiro('Digite o Preço R$:')
moeda.resumo(p, 10, 30)
