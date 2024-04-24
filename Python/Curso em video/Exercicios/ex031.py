n1 = int(input('Iai Quantos km foi rodado na sua viagem?'))
if n1 <=200:
    print('A sua viagem vai custar R$0,50 por km rodado ja que você não rodou mais que 200km')
    n2 = 0.50*n1
    print('A sua viagem custou R${:.2f}'.format(n2))
else:
    print('A sua viagem vai custar R$0,45 Por km rodado ja que você rodou mais que 200km')
    n3 = 0.45*n1
    print('A sua viagem vai custar R${:.2f}'.format(n3))
