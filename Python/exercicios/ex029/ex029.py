print('Vamo lá, vai ter um radar aqui viu?, o permitido é ate 80km')
n0 = float(input('Qual a sua velocidade pra ver se você tomou uma multa '))
if n0>80:
    print('Vish tu foi multado meu nobre,bora calcular isso aqui')
    n1 = n0-80
    n2 = n1*7
    print('Sabendo que a multa vai custar 7 reais para cada km acima do permitido')
    print('Você deve pagar R${:.2f} de multa'.format(n2))
else:
    print('Pode ficar de boa meu nobre, tu n foi multado não, graças a Deus')
    print('Tu tava abaixo ou igual do permitido, tu tava a {:.0f}Km'.format(n0))
