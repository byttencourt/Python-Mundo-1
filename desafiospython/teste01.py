tempo = int(input('Que ano é seu carro? ex:1995: '))
ano = 2023 - tempo
if ano >= 20:
    print('Seu automóvel tem {} anos e pode receber placa Preta.'.format(ano))
else:
    print('Seu veículo tem {} anos e não pode ter placa preta.'.format(ano))
print('Fim')