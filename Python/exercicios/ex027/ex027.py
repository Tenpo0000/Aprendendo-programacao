n1 = str(input('Digite seu nome completo')).strip()
n2 = n1.split()
print ('Primeiro nome é: {}'.format(n2[0]))
print ('Ultimo nome é: {}'.format(n2[len(n2)-1]))
