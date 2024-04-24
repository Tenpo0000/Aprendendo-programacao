Dia = int(input('Por quantos dias você usou o carro? '))
Km = float(input('Quantos quilometros você rodou? '))
n1 = Dia*60
n2 = Km*0.15
n3 = n1+n2

print('Como você rodou por {} dias e andou {}Km você deve pagar R${:.2f}'.format(Dia,Km,n3))
print('Sendo R${:.2f} Pelos dias e R${:.2f} Pelos Km rodados'.format(n1,n2))
print('Total de R${:.2f}'.format(n3))
