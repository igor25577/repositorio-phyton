pilha = []
expr = str(input('Digite uma expressão matematica : '))
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
if len(pilha) == 0:
    print('Sua expressão está CORRETA !')
else:
    print('Sua expressão está INCORRETA !')