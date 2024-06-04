import random
r = random.randrange(0,5)
print('Tente acertar o numero que eu pensei entre 0 a 5')
n1 = int(input('Qual o numero que eu pensei?'))
if n1 == r:
    print('Parabéns você acertou o numero {},que cagada'.format(r))
else:
    print('HAHAHA,você errou,a respota era {}'.format(r))
