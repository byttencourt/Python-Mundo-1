num = int(input('Digite um numero entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analizando o número {}.'.format(num))
print('Milhar: {}.'.format(m))
print('Centena {}.'.format(c))
print('Dezena {}.'.format(d))
print('Unidade {}.'.format(u))

