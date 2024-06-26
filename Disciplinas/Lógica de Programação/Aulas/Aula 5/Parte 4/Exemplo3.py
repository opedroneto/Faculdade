'''

Programa para verificar se uma senha digitada é forte
  - Mínimo de 8 caracteres
  - Pelo menos uma letra maiúscula
  - Pelo menos um dígito entre 0-9
  - Pelo menos um caractere de pontuação

O pacote string tem algumas constantes que podem ajudar:
  - string.uppercase: letras maiúsculas
  - string.digits: dígitos de 0 a 9
  - string.punctuation: caracteres de pontuação

'''

import string

senha = input("Senha: ")

maiuscula = False
digito = False
pontuacao = False

if len(senha) < 8:
    print("Erro: senha muito curta!")
else:
    for letra in senha:
        if letra in string.ascii_uppercase:
            maiuscula = True
        if letra in string.digits:
            digito = True
        if letra in string.punctuation:
            pontuacao = True

    if maiuscula == False or digito == False or pontuacao == False:
        if maiuscula == False:
            print("Erro: senha não tem maiúsculas")
        if digito == False:
            print("Erro: senha não tem dígitos")
        if pontuacao == False:
            print("Erro: senha não tem caractere de pontuação")
    else:
        print("Senha válida!")
