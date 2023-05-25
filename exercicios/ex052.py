from datetime import date
atual = date.today().year
print('Olá, você está no site da confederação nacional de natação,')
an = int(input('informe em que ano você nasceu :'))
id = atual - an
print('Nascido em {} você tem {} anos de idade'.format(an,id))
if id <= 9:
    print('Você tem {} ano(s) e se encaixa na categoria MIRIM'.format(id))
elif id <= 14:
    print('Você tem {} anos e se encaixa na categoria INFANTIL'.format(id))
elif id <= 19:
    print('Você tem {} anos e se encaixa na categoria JUNIOR'.format(id))
elif id <= 25:
    print('Você tem {} anos e se encaixa na categoria SÊNIOR'.format(id))
else:
    print('Você tem {} anos e se encaixa na categoria MASTER'.format(id))