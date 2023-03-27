alt = float(input('Qual a Altura da parede? '))
larg = float(input('Qual a largura da parede? '))
area = alt * larg
tint = area / 2
print('Uma parede com {}m de altura e {}m de largura, equivale a {} m2.\nNecessita de {} Litros de tinta para cobrir esta área.'.format(alt, larg, area, tint))
