'''

Programa para mostrar as iniciais de um nome com os sobrenomes, digitados
em uma única string

José Roberto Pereira

'''

nome = input("Digite um nome completo: ")

inicio = True
for letra in nome:
    if inicio:
        print(f"{letra}. ", end="")
        inicio = False
    elif letra == " ":
        inicio = True
