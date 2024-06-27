'''

Escreva um programa que leia uma quantidade desconhecida de números. A seguir,
o programa deve contar e escrever a quantidade de valores pertencentes aos 
seguintes intervalos: [0;25] [26;50] [51;75] [76;100]. A entrada de dados deve
terminar quando for lido um número negativo. Ao final o programa deve exibir
ainda a quantidade de valores lidos.

'''

total = 0
cont0_25 = 0
cont26_50 = 0
cont51_75 = 0
cont76_100 = 0

while True:
    print("Informe um valor negativo para encerrar a repetição.")
    valor = int(input("Informe um valor inteiro: "))
    if valor < 0:
        print("Fim do programa.")
        break
    if valor <= 25:
        cont0_25 += 1
    elif valor <= 50:
        cont26_50 += 1
    elif valor <= 75:
        cont51_75 += 1
    elif valor <= 100:
        cont76_100 += 1
    total += 1

print("=============================================")
print("Quantidade de valores digitados: ", total)
print("Quantidade de valores no intervalo [0;25]: ", cont0_25)
print("Quantidade de valores no intervalo [26;50]: ", cont26_50)
print("Quantidade de valores no intervalo [51;75]: ", cont51_75)
print("Quantidade de valores no intervalo [76;100]: ", cont76_100)
