nome = str(input('Digite o seu nome: ')).strip()
print('Nome: {}.'.format(nome))
n = nome.split()
print('Olá {}, prazer te conhecer.'.format(nome))
print('Primeiro: {}.'.format(n[0]).title())
print('Último: {}.'.format(n[len(n)-1]).title())

