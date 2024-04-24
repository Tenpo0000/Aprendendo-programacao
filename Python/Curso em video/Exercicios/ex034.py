print('O GERENTE FICOU MALUCO TA DANDO AUMENTO PRA GERAL')
n1 = float(input('Quanto você ganha pra gente calcular seu sálario?'))

if n1 > 1250.50:
    n2 = n1*10/100
    print('O seu aumento vai ser de 10% porque você recebe acima de R$1250,50')
    print('Tendo isso em mente você vai receber R${:.2f} a mais'.format(n2))
    print('No total você vai passar a receber R${:.2f} ao todo'.format(n2+n1))

else:
    n3 = n1*15/100
    print('O seu aumento vai ser de 15% porque você recebe abaixo ou igual a R$1250,50')
    print('Tendo isso em mente você vai receber R${:.2f} a mais'.format(n3))
    print('No total você vai passar a receber R${:.2f} ao todo'.format(n3+n1))
