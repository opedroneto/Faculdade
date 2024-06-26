'''

Faça um programa que leia a altura de uma pessoa em metros e o seu genero
(use 1 para feminino e 2 para masculino). A seguir, o programa deve escrever o
peso ideal dessa pessoa conforme descrito a seguir: 

- Para homens, o peso ideal correspondente a 72.7 * altura - 58
- Para mulheres, use 62.1 * altura - 44.7

'''

altura = float(input("Informe a sua altura: "))
genero = int(input("Digite 1 para genero feminino ou 2 para genero masculino: "))

if genero == 1 : peso = 62.1 * altura - 44.7
if genero == 2 : peso = 72.7 * altura - 58

if genero != 1 and genero != 2 :
  print("Genero invalido. Peso ideal nao calculado.")
  peso = 0

print("Peso ideal: ", peso)