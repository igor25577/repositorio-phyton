import random
n1 = str(input('primeiro aluno:'))
n2 = str(input('segundo aluno:'))
n3 = str(input('terceiro aluno:'))
n4 = str(input('quarto aluno'))
lista1 = [n1, n2, n3, n4]
escolhido1 = random.choice(lista1)
print('o aluno escolhido foi:{}'.format(escolhido1))

print('ou')

from random import choice
p1 = str(input('primeira pessoa:'))
p2 = str(input('segunda pessoa:'))
p3 = (input('terceira pessoa:'))
p4 = str(input('quarta pessoa:'))
lista2 = [p1, p2, p3, p4]
escolhido2 = choice(lista2)
print('a pessoa escolhido foi:{}'.format(escolhido2))
