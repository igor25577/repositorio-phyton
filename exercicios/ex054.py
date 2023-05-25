p = float(input('Qual o seu peso ?(Kg)'))
a = float(input('Qual a sua altura ?(M)'))
imc = p/(a*a)
print('Com o peso de {} e a altura de {} seu IMC é {:.1f}'.format(p,a,imc))
if imc < 16:
    print('Você está classificado com MAGREZA GRAU III ',end='')
    print('Você precisa aumentar sua alimentação imediatamente')
elif imc <= 17:
    print('Você está classificado com MAGREZA GRAU II ',end='')
    print('Você deve começar a se alimentar bem')
elif imc <= 18.4:
    print('Você está classificado com MAGREZA GRAU I ',end='')
    print('Comece a prezar da alimentação')
elif imc <= 24.9:
    print('Você está classificado com EUTROFIA ',end='')
    print('Não se preocupe com o nome esquisito você está no peso ideal mantenha o padrão! ')
elif imc <= 29.9:
    print('Você está classificado com  SOBREPESO ',end='')
    print('Cuidado com sua alimentação ela pode estar desbalanceada')
elif imc <= 34.9:
    print('Você está classificado com OBESIDADE GRAU I ',end='')
    print('Comece a reeducar sua alimentação pois isso pode começar a afetar sua saude')
elif imc <= 39.9 :
    print('Você está classificado com OBESIDADE GRAU II ',end='')
    print('Tome muito cuidado pois sua saude corre risco')
elif imc > 40 :
    print('Você está clasificado com OBESIDADE GRAU III ',end='')
    print(' também conhecida como morbida Muito cuidado sua vida corre risco!')
