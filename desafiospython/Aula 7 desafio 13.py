print('='*20)
print('ESTIMATIVA DE AUMENTO')
sal = float(input('Qual seu salário atual? '))
nsal = sal + (sal * 15 / 100)
print('Um funcionario que ganha R${:.2f}, Assim seu novo salário será de R${:.2f} Reais'.format(sal, nsal))
