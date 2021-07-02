# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('Preço do produto: '))
d = p - (p * 5 / 100)

print('Seu novo preço é de R${}'.format(d))