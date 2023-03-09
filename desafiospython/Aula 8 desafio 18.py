from math import radians, sin, cos, tan
angulo = float(input('Digite um o valor do Angulo: '))
sen = sin(radians(angulo))
print('O seno de {}º é {:.2f}'.format(angulo, sen))
cos = cos(radians(angulo))
print('O cosseno de {}º, é {:.2f}.'.format(angulo, cos))
tan = tan(radians(angulo))
print('A tangente de {}º, é {:.2f}.'.format(angulo, tan))

