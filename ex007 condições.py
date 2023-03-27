n1 = float(input('Qual a primeira nota? '))
n2 = float(input('Qual a segunda nota? '))
m = (n1 + n2) / 2
print('A sua média é {:.1f}'.format(m))
if m >= 7:
    print('Voce foi Aprovado!')
else:
    print('Você foi Reprovado')