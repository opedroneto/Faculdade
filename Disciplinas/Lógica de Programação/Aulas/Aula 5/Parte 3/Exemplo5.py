'''

Operador de pertenciamento

'''

texto1 = input("Digite uma frase: ")
texto2 = input("Digite uma palavra: ")

if texto2 in texto1:
    print(f"{texto2} está na frase.")
else:
    print(f"{texto2} não está na frase...")
