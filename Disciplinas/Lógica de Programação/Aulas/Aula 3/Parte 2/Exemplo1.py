'''

Implemente um programa que leia 3 valores e escreva o maior deles.

'''

v1 = int(input("Informe o primeiro valor: "))
v2 = int(input("Informe o segundo valor: "))
v3 = int(input("Informe o terceiro valor: "))

if v1 > v2 and v1 > v3 : maior = v1
if v2 > v1 and v2 > v3 : maior = v2
if v3 > v1 and v3 > v2 : maior = v3

print("Maior: ", maior)

# OUTRA OPCAO DE CODIGO

v1 = int(input("Informe o primeiro valor: "))
v2 = int(input("Informe o segundo valor: "))
v3 = int(input("Informe o terceiro valor: "))
v4 = int(input("Informe o quarto valor: "))

maior = v1

if v2 > maior : maior = v2
if v3 > maior : maior = v3
if v4 > maior : maior = v4

print("Maior: ", maior)