n1 = str(input('Fala seu nome ai vagabundo')).lower().strip()
n3 = n1.count('a')
n4 = n1.find('a')
n5 = n1.rfind('a')
print('A letra (A) aparece {} Vezes'.format(n3))
print('A letra (A) aparece pela primeira vez na posição:{}'.format(n4+1))
print('A letra (A) aparece pela ultima vez na posição:{}'.format(n5+1))
