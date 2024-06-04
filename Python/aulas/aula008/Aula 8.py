import math,random
f = float(input('Digite um numero flutuante '))
print ('o numero inteiro de {} é {:.0f}'.format(f,f))

n = float(input('Fale o resultado do primeiro cateto'))
n1 = float(input('Fale o outro cateto'))
r = (n**2)+(n1**2)
r1 = math.sqrt(r)
print ('o cateto da hipotenusa é {}'.format(math.floor(r1)))

um = str(input('participantes do primeiro grupo'))
dois = str(input('e do segundo grupo?'))

print(random.binomialvariate(um,dois))
