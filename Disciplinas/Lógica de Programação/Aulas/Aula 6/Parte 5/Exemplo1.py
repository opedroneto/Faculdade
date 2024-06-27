'''

Construa um programa que escreve o fatorial dos 100 primeiros inteiros

'''

numero = 0
while numero <= 99:
    fat = 1
    aux = 2
    while aux <= numero:
        fat *= aux
        aux += 1
    print("O fatorial de ", numero, " eh ", fat)
    numero += 1
