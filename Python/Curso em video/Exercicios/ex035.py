print('Me informe 3 retas para ver se da pra formar um triangulo')
n1 = float(input('Primeira reta:'))
n2 = float(input('segunda reta:'))
n3 = float(input('Terceira reta:'))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n2 + n1:
    print('Os seguimentos podem formar um triangulo')
else:
    print('Não pode formar um triangulo')
