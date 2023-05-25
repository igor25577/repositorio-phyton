aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Media: '))
print('-=-' * 10)
print(f'- O nome do aluno é: {aluno["nome"]}')
print(f'- A media foi: {aluno["media"]}')
if aluno['media'] >= 5:
    print('- Situação aprovado')
else:
    print('- Situação igual a reprovado')
