frase = str(input('Digite uma Frase: ').upper()).strip()
print('Vezes que aparece a letra "A": {}'.format(frase.count('A')))
print('A primeira vez que a letra aparece é na {}º posição.'.format(frase.find('A')+1))
print('A ultima vez que o caractere é encontrado seria na {}º posição.'.format(frase.rfind('A')+1))

