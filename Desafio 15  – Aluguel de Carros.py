print('='*20)
print('LOCADORA NINOSEG')
print('='*20)
dias = int(input('Qual a quantidade de dias que o veículo foi utilizado? '))
km = int(input('Qual a quantidade de km percorrido pelo Veículo? '))
tdias = dias * 60
tkm = km * 0.15
print('='*20)
print('O custo por {} dia(s), de uso do veículo é de R${:.2f}.'.format(dias, tdias))
print('Você percorru um total de {}kms, totalizando R${:.2f}.'.format(km, tkm))
print('o custo total da locação é de R${:.2f}.'.format(tkm+tdias))
