'''

Construa um programa que leia dois valores inteiros e escreva na tela:
a) a soma
b) a diferença
c) a média
d) a distancia (valor absoluto da diferença)
e) o maior dos dois (use maior = a+b+a-b/2)
f) o menor dos dois (use menor = a+b-a-b/2)

'''
import math

valor1 = int(input("Digite o primeiro valor inteiro: "))
valor2 = int(input("Digite o segundo valor inteiro: "))

soma = valor1 + valor2
diferenca = valor1 - valor2
media = (valor1 + valor2) / 2
distancia = math.fabs(valor1 - valor2)
maior = (valor1 + valor2 + math.fabs(valor1-valor2))/2
menor = (valor1 + valor2 - math.fabs(valor1-valor2))/2

print("Soma: ", soma)
print("Diferença: ", diferenca)
print("Media: ", media)
print("Distancia: ", distancia)
print("Maior: ", maior)
print("Menor: ", menor)
