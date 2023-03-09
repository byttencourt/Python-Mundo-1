import random
v = int(input('Digite a velocidade em km/h: '))
if v > 80:
    print('Parabéns! Voce acaba de ser multado por trafegar a {} Km/h.'.format(v))
    multa = (v - 80) * 7
    print('O valor da autuação é de R${:.2f}.'.format(multa))
else:
    print('Você está a {} km/h continue assim!'.format(v))
