from random import randint
n = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
print(f'O programa sorteou os seguintes numeros {n}')
maior = n[0]
menor = n[0]
print(f'O maior numero sorteado foi {max(n)}')
print(f'O menor numero sorteado foi {min(n)}')
