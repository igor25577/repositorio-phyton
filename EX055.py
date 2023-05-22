print('{:=^40}'.format('LOJAS BEBETA'))
v = float(input('Valor das compras: R$'))
va = v * 90/100
vac = v * 95/100
pc2 = v/2
print('FORMAS DE PAGAMENTO')
print('[1] A vista dinheiro/cheque')
print('[2] A vista no cartão')
print('[3] Parcelado 2x no cartão')
print('[4] Parcelado 3x ou mais ')
fp = int(input('Selecione a forma de pagamento:'))
if fp == 1:
    print('Ao pagar a vista no dinheiro/cheque você tem um desconto de 10% ')
    print('O valor de R${:.2f} passa a ser R${:.2f}'.format(v,va))
elif fp == 2:
    print('Ao pagar a vista no cartão você recebe um desconto de 5% ',end='')
    print('E o valor passa a ser R${:.2f} com o desconto'.format(vac))
elif fp == 3:
    print('O valor parcelado em duas vezes é duas parcelas de R${:.2f}'.format(pc2))
elif fp == 4:
    print('o valor parcelado em 3x ou mais tem juros de 20%')
    np = int(input('informe o numero de parcelas:'))
    vp = (v / np) * 120 / 100
    print('Dividindo em {} vezes dá um valor de R${:.2f} cada parcela'.format(np,vp))
else:
    print('{:X^40}'.format(' OPÇÃO INVALIDA REFASSA O PROCESSO '))
