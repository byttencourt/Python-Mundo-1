d = float(input('Qual a distancia da viagem? '))
if d >= 200:
    p = (d * 0.45)
else:
    p = (d * 0.5)
print('Valor da Passagem para uma viagem de {}km é R${:.2f}.'.format(d, p))
