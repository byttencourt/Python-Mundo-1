s = float(input('Digite o salario: '))
if s > 1250:
    a = s + (s * 10/100)
    print('Seu novo salário será R$ {:.2f}.'.format(a))
else:
    a = s + (s * 15/100)
    print('Seu novo salário terá 15% passando a ser R$ {:.2f}.'.format(a))
