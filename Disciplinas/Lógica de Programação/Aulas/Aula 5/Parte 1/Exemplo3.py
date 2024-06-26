'''

Comece com um "chute", n
Repita uma certa quantidade de vezes
  - O próximo "chute" será a media entre n e x/n
Exiba o "chute" no final 

'''

num = int(input("Valor desejado: "))
total = int(input("Qtd. de repetições: "))

aprox = 1
for cont in range(1, total+1):  # repete "total" vezes
    aprox = (aprox + num/aprox) / 2
    print(f"{cont:3}: {aprox:.5f}")

print(f"Raiz aproximada: {aprox:.5f}")
