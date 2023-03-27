from random import randint
from time import sleep
n = int(input('Digite um número entre 0 e 5: '))
r = randint(1, 5)
print('Pensando...')
sleep(1)
print('Você digitou: {}.\nnumero sorteado: {}.'.format(n, r))
if n == r:
    print('Parabéns você venceu!')
else:
    print('Que pena Tente novamente!')
