# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere U$$1.00 = R$3.27

v = float(input('Quanto dinheiro você tem na carteira R$: '))

d = v / 3.27

print('O valor convertido é U$${:.2f}'. format(d))