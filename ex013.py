#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.


s = float(input('Digite seu salário R$: '))

a = s + (s*15/100)

print('Seu novo salário é R$ {}'.format(a))