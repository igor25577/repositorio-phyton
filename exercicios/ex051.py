n1 = float(input('Digite a primeira nots que tirou:'))
n2 = float(input('Digite a segunda nota que tirou:'))
nm = (n1+n2)/2
print('Sua primeira nota foi {:.1f} e sua segunda nota foi {:.1f} sendo assim sua media é {:.1f}'.format(n1,n2,nm))
if nm<5:
    print('Você está REPROVADO !')
elif nm == 5 or nm<7:
    print('Você está em RECUPERAÇÃO !')
elif nm == 7 or nm>7:
    print('Parabéns você foi APROVADO !')
