'''

Implemente um programa que escreve os n primeiros números primos

'''

quant = int(input("Informe a quantidade de números primos: "))
while quant <= 0:
    print("Valor inválido. A quantidade deve ser positiva.")
    quant = int(input("Informe a quantidade de números primos: "))

num = 2
contPrimos = 0
while contPrimos <= quant:
    contaDivisores = 0
    d = 1
    while d <= num:
        if num % d == 0:
            contaDivisores += 1
        d += 1
    if contaDivisores == 2:
        print(num)
        contPrimos += 1
    num += 1
