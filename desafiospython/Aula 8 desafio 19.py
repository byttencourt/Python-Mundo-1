from random import choice
a1 = input('Digite o Primeiro nome: ')
a2 = input('Digite o segundo nome: ')
a3 = input('Digite o terceiro nome: ')
a4 = input('Digite o Quarto nome: ')
lista = [a1, a2, a3, a4]
escolha = choice(lista)
print('E o nome do sortudo a apagar o quadro negro é {}'.format(escolha))

