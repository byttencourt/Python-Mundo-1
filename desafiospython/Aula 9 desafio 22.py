print('='*20)
nome = str(input('Digite seu nome Completo: ')).strip()
print('Em maúscula: {}'.format(nome.upper()))
print('Em minúscula: {}'.format(nome.lower()))
separa = nome.split()
print('Seu nome possui um total de {} letras.'.format(len(nome) - nome.count(' ')))
print('O primeiro nome {}, possui um total de {} caracteres.'.format(separa[0], len(separa[0])))



