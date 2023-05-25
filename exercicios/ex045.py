print('\033[7;30;44m Olá mundo!\033[m')
a = 3
b = 5
print('Os valores são \033[30m{}\033[m e \033[33m{}\033[m'.format(a, b))
n = 'Igor'
print('Prazer em te conhecer {}{}{}'.format('\033[4;34;40m', n,'\033[m]' ))
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('É um prazer te conhecer {}{}{}'.format(cores['pretoebranco'], n, cores['limpa']))
