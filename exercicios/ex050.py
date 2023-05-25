from datetime import date
atual = date.today().year
a = int(input('Ano de nascimento:'))
id = atual-a
print('Nascido em {} você tem {} anos'.format(a,id))
if id > 18:
    saldo = id-18
    print('Você tem {} ano(s) e jÁ passou {} ano(s) da idade de se alistar!'.format(id,saldo))
    print('Seu alistamento foi no ano de {}'.format(atual-saldo))
elif id < 18:
    saldo = 18-id
    print('Você tem {} ano(s) e NÃO passou da epoca de se alistar ainda faltam {} ano(s)'.format(id,saldo))
    print('E seu ano de alistamento será no ano de {}'.format(atual+saldo))
else:
    print('você tem {} e está na idade EXATA de alistamento'.format(id))
