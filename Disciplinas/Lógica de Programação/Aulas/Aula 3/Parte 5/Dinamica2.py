'''

Elabore um programa que leia 3 notas, calcule e escreva a media ponderada
delas considerando os pesos 5, 2.5 e 2.5. A maior nota deve ter peso 5.

'''

nota1 = float(input("Informe a nota 1: "))
nota2 = float(input("Informe a nota 2: "))
nota3 = float(input("Informe a nota 3: "))

if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10 or nota3 < 0 or nota3 > 10:
    print("Notas inválidas. Elas devem estar no intervalo [0; 10]")
else:
    maior = nota1
    if nota2 > maior:
        maior = nota2
    if nota3 > maior:
        maior = nota3
    media = 0.5 * maior + 0.25 * (nota1+nota2+nota3-maior)
    print("Média ponderada: ", media)
