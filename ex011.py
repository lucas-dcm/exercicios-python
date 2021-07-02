# Faça um programa que leia a largura e a altura de uma parede em metros.
# Calcule a sua área e a quantidade de tinta para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

l = float(input('Digite a largura da parede em metros: '))
a = float(input('Digite a altura da parede em metros: '))

ar = l * a 

q = ar * (2**(1/2))

print('Sua área é {}. Você precisa de {:.2f} litros de tinta para terminar a pintura.'.format(ar, q))

