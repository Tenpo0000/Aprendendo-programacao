import math
n = float(input('Digite o ângulo desejado '))
tan = math.tan(math.radians(n))
print ('o ângulo de {} é igual a TANGENTE DE {:.2f}'.format(n,tan))
cos = math.cos(math.radians(n))
print ('o ângulo de {} é igual o COSSENO DE {:.2f}'.format(n,cos))
seno =  math.sin(math.radians(n))
print ('o ângulo de {} é igual o SENO DE {:.2f}'.format(n,seno))
