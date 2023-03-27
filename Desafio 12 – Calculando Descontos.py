p = float(input('Qual valor da mercadoria? '))
d = int(input('Qual a porcentagem de desconto? '))
por = p - (p*d/100)
print('Na liquidação o produto que custava R${:.2f}, com {}% de ficam por apenas R${:.2f}.'.format(p, d, por))

