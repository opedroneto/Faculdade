'''

Implemente um programa que leia um valor inteiro entre 1 e 7, correspondente
ao dia da semana. O programa deve escrever o dia da semana por extenso 
correspondente ao valor lido. Por exemplo, se o usuário escrever 1, o programa
deve exibir Domingo.

'''

valor = int(input("Informe um número de 1 a 7: "))
if valor < 1 or valor > 7:
    print("Número inválido.")
else:
    if valor == 1:
        print("Domingo")
    if valor == 2:
        print("Segunda")
    if valor == 3:
        print("Terça")
    if valor == 4:
        print("Quarta")
    if valor == 5:
        print("Quinta")
    if valor == 6:
        print("Sexta")
    if valor == 7:
        print("Sábado")
