l = float(input('Largura da parede em mentros'))
a = float(input('Altura da parede em metros'))
aa = l*a
t = aa/2
print('Sua parede tem: \naltura de {} metros\nLargura de {} metros\nSua Área é de {}m²\nEntão é preciso de {:.2f} Litros de tinta para pintar sua parede'.format(a,l,aa,aa/2))
