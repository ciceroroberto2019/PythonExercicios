d = int(input('Quantos dias alugado?'))
k = float(input('Quantos Km rodado:'))
t = (d * 60) + (k * 0.15)
print('Você alugou o carro por {} dias e rodou {}km,  total à pagar R${:.2f}'.format(d, k, t))