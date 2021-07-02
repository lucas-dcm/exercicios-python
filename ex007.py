#Desenvolva um programa que leia  duas notas de um aluno, calcule e mostre sua média.

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1+n2)/2

print('Sua média é igual a {:.1f}'.format(m))