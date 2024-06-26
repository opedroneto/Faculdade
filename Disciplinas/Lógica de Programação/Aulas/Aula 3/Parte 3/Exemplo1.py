'''

Elabore um programa que leia uma nota do intervalo [0; 10] (garanta isso),
verifique e escreva o conceito correspondente conforme a tabela abaixo:

nota            conceito
9 a 10          A
7 a 8,9         B
5 a 6,9         C
3 a 4,9         D
abaixo de 3     E

'''

nota = float(input("Informe a nota"))

if nota < 0 or nota > 10:
    print("Erro. Entrada inválida.")
    print("A nota deve estar no intervalo entre [0; 10]")
else:
    if nota >= 9 and nota <= 10:
        print("Conceito A")
    if nota >= 7 and nota < 9:
        print("Conceito B")
    if nota >= 5 and nota < 7:
        print("Conceito C")
    if nota >= 3 and nota < 5:
        print("Conceito D")
    if nota >= 0 and nota < 3:
        print("Conceito E")
