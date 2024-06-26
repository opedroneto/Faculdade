'''

Passando diretamente por todos os caracteres de uma string

'''

texto = input("Digite uma frase: ")
for caractere in texto:
    print(caractere)


'''

Passando por todos os caracteres de uma string, usando acesso por índice

'''

texto = input("Digite uma frase: ")
for posicao in range(len(texto)):
    # print(texto[posicao])
    print(f"{posicao}: {texto[posicao]}")
