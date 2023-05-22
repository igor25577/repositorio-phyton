palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR',
           'MERCADO', 'PROGRAMADOR', 'FUTURO')
for p in palavras:
    print(f'\n Na palavra {p} tem as vogais:',end=' ')
    for letras in p:
        if letras.upper() in 'AEIOU':
            print(letras,end='')
print('\n','-=-' * 40)
print(' FIM DO PROGRAMA...')
