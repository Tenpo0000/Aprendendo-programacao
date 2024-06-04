n = int(input('Fale uma medida em metros'))
print('{} Metros correspondem a:'.format(n))
print('{} km\n{} hn\n{} dan\n{} dn\n{} cm\n{} mm'.format(n/1000,n/100,n/10,n*10,n*100,n*1000))