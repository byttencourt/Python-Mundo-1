from random import shuffle
print('='*20)
a1 = input('Digite o nome do Primeiro aluno: ')
a2 = input('Digite o nome do Segundo aluno: ')
a3 = input('Digite o nome do Terceiro aluno: ')
a4 = input('Digite o nome do Quarto aluno: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('LISTA DE SORTEADOS')
print('Os alunos sorteados são {}.'.format(lista))



