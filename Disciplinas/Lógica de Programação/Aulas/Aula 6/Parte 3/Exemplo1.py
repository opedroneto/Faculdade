'''

Chico tem 1,50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1,10 metro e 
cresce 3 centímetros por ano. Construa um programa que calcule e exiba quantos anos 
serão necessários para que Zé seja maior que Chico.

'''

altChico = 150
altZe = 110
anos = 0

while altZe <= altChico:
  altChico += 2
  altZe += 3
  anos += 1
print(f"Anos: {anos}")