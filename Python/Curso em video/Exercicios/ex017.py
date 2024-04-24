import math
n1 = float(input('Qual o valor do primeiro cateto? '))
n2 = float(input('E qual o do cateto adjacente? '))
r = math.hypot(n1,n2)
print('O cateto da hipotenusa é igual a {:.2f}'.format(r))
