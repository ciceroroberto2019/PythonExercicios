print('='*20, 'Exercicio 007', '='*20)
n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
s = n1+n2
#ou pode ser feito s = (n1 + n2)/2
print('A  primeira nota foi {:.1f} a segunda nota foi {:.1f}, total {:.1f} e sua média é {:.1f}'.format(n1, n2, s, s/2))
