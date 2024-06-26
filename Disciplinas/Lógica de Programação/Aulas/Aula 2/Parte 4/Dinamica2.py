'''

Implemente um programa que leia um valor n, calcule e escreva n2, n3 e n4.

'''

import math

print("Informe o valor de n: ")
n = float(input())
n2 = math.pow(n, 2)
n3 = math.pow(n, 3)
n4 = math.pow(n, 4)

print("n elevado a 2: ", n2)
print("n elevado a 3: ", n3)
print("n elevado a 4: ", n4)

# SEGUNDA OPCAO DE CODIGO

print("Informe um valor: ")
valor = float(input())
print("Quadrado do valor: ", valor ** 2)
print("Cubo do valor: ", valor ** 3)
print("Valor na quarta: ", valor ** 4)
