#cor.l = {0, black, red, green, yellow, magenta, cyan, grey, white}
#cor.lb = {0,1,2,3,4,5}
import cor
print('{}= = = = = =  DESAFIO 02 = = = = = = ={}'.format(cor.l['red'], cor.l['0']))
dia = input ('Dia = ')
mes = input ('Mês = ')
ano = input ('Ano = ')
print('{}Você nasceu no dia {} de {} de {}. Correto?{}'.format(cor.lb['1'], dia, mes, ano, cor.lb['0']))
