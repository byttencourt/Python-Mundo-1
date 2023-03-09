#cor.l = {0, black, red, green, yellow, magenta, cyan, grey, white}
#cor.lb = {0,1,2,3,4,5}
# codigo modificado com adição de cores nas letras: Adicionar {} e .format(cor['n'])
import cor
print('{}=-=-=-=-=- DESAFIO 01 -=-=-=-=-=-={}'.format(cor.l['magenta'], cor.l['0']))
nome = input('{}Qual é o seu nome?{}'.format(cor.l['green'], cor.l['0'])).strip().title()
print('Olá {}{}{} Prazer em te conhecer!'.format(cor.lb['1'], nome, cor.lb['0']))
