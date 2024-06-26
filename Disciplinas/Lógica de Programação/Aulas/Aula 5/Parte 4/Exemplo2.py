'''

Faça um programa para contar a quantidade de vogais presentes em uma string
Exemplo: teste de contagem ---> 6 vogais

'''

texto = input("Digite uma frase: ")

vogais = "aeiouAEIOU"
totalVogais = 0

for letra in texto:
    if letra in vogais:
        totalVogais += 1

print(f"Quantidade de vogais: {totalVogais}")
