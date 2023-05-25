s=float(input('informe seu salario para que informemos quanto ele sera após o aumento:'))
print('o seu salario era:{} reais e apos o aumento de 15% passou a ser:{} reais'.format(s,s*1.15))

s=float(input('informe seu salaria que faremos o calculo do aumneto:'))
ns=s+(s*15/100)
print('o salario de:{:.2f} com o aumento de 15% foi para:{:.2f}'.format(s,ns))
