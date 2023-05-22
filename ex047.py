print('Olá! Eu sou um simulador de empréstimos imobiliario')
print('Por favor preencha os campos abaixo para que eu possa informar se será possivel realizar o empréstimo')
v = float(input('Qual o valor da propiedade que deseja comprar ? R$'))
s = float(input('Qual o valor do seu salario mensal ? R$'))
tempo = int(input('Em quantos anos pretende financiar ?'))
tempm = tempo*12
vm = v/tempm
print('Para comprar uma casa de R${:.2f} em {} anos'.format(v,tempo), end='')
print(' a prestação mensal será de R${:.2f}'.format(vm))
if vm<= s*0.3:
    print('Parabens você acaba de receber creditos para comprar sua propriedade!')
else:
    print('sentimos muito mas seu pedido foi NEGADO')
