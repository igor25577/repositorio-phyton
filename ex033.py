n = str(input('Digite seu nome completo:')).strip()
nome = n.split()
print('Prazer em te conhecer {}'.format(n))
print('Seu primeiro nome é: {}, correto ?'.format(nome[0]))
print('E o seu ultimo nome é: {}, correto ?'.format(nome[len(nome)-1]))

