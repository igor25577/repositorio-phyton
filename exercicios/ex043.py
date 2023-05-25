s = float(input('Qual o valor do seu salario?'))
if s <= 1250.00:
    print('Seu novo salario será:{:.2f}R$'.format(s*1.15))
else:
    print('Seu novo salario será de:{:.2f}R$'.format(s*1.10))
