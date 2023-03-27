n1 = int(input('n1: '))
n2 = int(input('n2: '))
n3 = int(input('n3: '))
ma = n1
if n2 > ma:
    ma = n2
if n3 > ma:
    ma = n3
print('maior = {}'.format(ma))
me = n1
if n2 < me:
    me = n2
if n3 < me:
    me = n3
print('menor= {}.'.format(me))
