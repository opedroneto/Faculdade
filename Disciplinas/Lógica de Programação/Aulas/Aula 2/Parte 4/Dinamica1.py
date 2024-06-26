'''

Enunciado 1

Faça um programa que leia o valor do raio, calcule e escreva a área de uma esfera. 
A área de uma esfera é dada por a = 4PIr2

'''

import math

print("Informe o valor do raio(r): ")
raio = float(input())
area = 4 * math.pi * math.pow(raio, 2)  # OU raio**2

print("Área da esfera: ", area)
