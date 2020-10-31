print('=' * 20, 'Exercicio 011', '=' * 20)
l = float(input('Informe a largura da parede: '))
a = float(input('Informe a altura da parede: '))
m4 = l * a
print('Sua parede tem {:.3f} m² e precisara de {:.3f} litros de tinta para pintar ela'.format(m4, m4/2))
