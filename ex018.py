from math import sin, radians, cos, tan
an = float(input('Digite o angulo que você deseja: '))
seno = sin(radians(an))
cosseno = cos(radians(an))
tangente = tan(radians(an))
print('O angulo de {} tem o SENO é {:.2f}'.format(an, seno))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(an, cosseno))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(an, tangente))