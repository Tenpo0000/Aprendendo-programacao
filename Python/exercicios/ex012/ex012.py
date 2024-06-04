n = float(input('Valor do produto'))
n1 = float(input('Quantos % de desconto esta o seu produto?'))
n2 = n*n1/100
print ('O seu produto que valia R${} com {}% de Desconto fica R${:.2f}'.format(n,n1,n-n2))
print('A diferença é de R${:.2f}'.format(n2))