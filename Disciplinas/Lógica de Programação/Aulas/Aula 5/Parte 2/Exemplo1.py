num = int(input("Valor desejado: "))
total = int(input("Qtd. de repetiçoes: "))

aprox = 1
anterior = 0
for cont in range(1, total + 1):
    aprox = (aprox + num / aprox) / 2
    print(f"{cont:3} {aprox:.5f}")
    dif = abs(aprox - anterior)
    if dif < 0.001:
        break
    anterior = aprox

print(f"Raiz aproximada: {aprox:.5f}")
