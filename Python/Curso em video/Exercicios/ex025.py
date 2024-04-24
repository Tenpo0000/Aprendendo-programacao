n1 = str(input('Qual o nome da sua cidade? ')).strip()
print('A palavra (Santos) se encontra no primeiro nome?:')
n2 = n1.lower()
print(n2[0:5] == 'santo')
