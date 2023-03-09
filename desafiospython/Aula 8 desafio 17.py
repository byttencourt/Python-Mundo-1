from math import hypot
print('='*20)
co = float(input('Digite um valor para o cateto oposto: '))
ca = float(input('Digite um valor para o cateto adjacente: '))
#hi = (co ** 2 + ca ** 2) ** (1/2)
hi = hypot(co,ca)
print('O valor do cateto oposto é de {:.2f}'.format(hi))


