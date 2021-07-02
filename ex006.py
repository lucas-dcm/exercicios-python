#Crie um algoritmo que leia um numero e mostre seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))
print('Seu número é {}. \nO dobro vale {}. \nO triplo vale {}. \nA raiz quadradada é igual a {:.2f}!'.format(n, (n*2), (n*3), pow(n,(1/2))))