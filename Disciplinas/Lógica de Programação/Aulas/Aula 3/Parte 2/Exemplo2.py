'''

Implemente um programa que leia 2 valores e os escreva em ordem

'''

v1 = int(input("Informe o primeiro valor: "))
v2 = int(input("Informe o segundo valor: "))

if v1 > v2:
  aux = v1
  v1 = v2
  v2 = aux

print(v1, v2)
print("Fim")