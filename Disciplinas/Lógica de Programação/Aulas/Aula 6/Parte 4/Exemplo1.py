'''

Repetição aninhada utilizando for
Tabuada 1-10

'''

for numero in range(1, 11):
    for valor in range(1, 11):
        print(numero, ' x ', valor, ' = ', numero * valor)
    print()

'''

Repetição aninhada utilizando while
Tabuada 1-10

'''

numero = 1
while numero <= 10:
    valor = 1
    while valor <= 10:
        print(numero, ' x ', valor, ' = ', numero * valor)
        valor += 1
    print()
    numero += 1
