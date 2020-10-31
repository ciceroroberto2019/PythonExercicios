from math import sqrt
cme = float(input('Informe o cateto menor: '))
cma = float(input('Informe oateo maior: '))
#hi = (cme ** 2 + cma ** 2)** (1/2)
#hi = math.hypot(cme,cma)
h = sqrt((pow(cme, 2))+(pow(cma, 2)))
print('A soma dos quadrados dos catetos é igual a {:.2f}'.format(h))
