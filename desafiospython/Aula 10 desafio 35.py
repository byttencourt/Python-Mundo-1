a = float(input('Digite l1: '))
b = float(input('Digite l2: '))
c = float(input('digite l3: '))
if a + b > c and a + c > b and b + c > a:
    print('é triangulo')
else:
    print('Não é triangulo')