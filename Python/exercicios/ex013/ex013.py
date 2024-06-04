n = float(input('Quanto o funcionario ganha? R$'))
r = (n*15/100)
t = r+n

print('O funcionario que ganhava R${:.2f} Com aumento de 15% do seu salario vai começar a receber R${:.2f}'.format(n,t))
print('A diferença é de R${:.2f}'.format(r))
