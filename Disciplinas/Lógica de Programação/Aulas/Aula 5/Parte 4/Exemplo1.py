'''

Faça um programa para verificar se uma string digitada corresponde ao contrário (palíndromo)
Exemplo: reviver <---> reviver

'''

# Solução 1

texto = input("Digite uma frase: ")

dif = False
for pos in range(len(texto)//2):
    if texto[pos] != texto[-1-pos]:
        dif = True
        break

if dif:
    print("A frase não é um palíndromo...")
else:
    print("A frase é um palíndromo!")


# Solução 2

texto = input("Digite uma frase: ")
print(f"Invertida: {texto[::-1]}")

if texto != texto[::-1]:  # string ao contrario
    print("A frase não é um palíndromo...")
else:
    print("A frase é um palíndromo!")
