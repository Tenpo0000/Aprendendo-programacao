print ('Vamos ver se você nasceu em um ano bissexto')
n1 = int(input('Qual ano você nasceu?'))
if (n1 % 4==0 and n1 % 100!=0) or (n1 % 400==00):
    print('O ano {} é bissexto'.format(n1))
    print('Ele é considerado bissexto porque é dividido por 4 e 400 e não é divisivel  100')
else:
    print('o ano {} não é bissexto'.format(n1))
    print('Ele não é bissexto porque ele não é dividido por 4 e 400 e é divisivel por 100')

