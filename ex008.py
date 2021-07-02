# Escreva um programa que leia um valor em metros e o exiba convertido em cm e mm.

medida = float(input('Digite sua medida para ser convertida: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10

dm = medida * 10
cm = medida * 100
mm = medida * 1000

print('Sua medida é igual a {}.'.format(medida))
print('Convertido em km é igual a {}.\nConvertido em hm é igual a {}.\nConvertido em dam é igual a {}.\nConvertido em dm é igual {}.\nConvertido em cm é igual {}.\nConvertido em mm é igual {}.'.format(km, hm, dam, dm, cm, mm))


#quilômetro (km)	hectômetro (hm)	decâmetro (dam)	metro (m)	decímetro (dm)	centímetro (cm)	milímetro (ml)
