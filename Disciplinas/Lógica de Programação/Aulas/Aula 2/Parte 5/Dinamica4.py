'''

Implemente um programa que lê um (único) valor inteiro de 4 dígitos. A seguir, esse 
programa deve escrever um inteiro que corresponde ao valor lido na ordem inversa.
(Exemplo: 1234 --> 4321)

'''

valor = int(input("Digite um valor inteiro de 4 digitos: "))
milhar = valor//1000
resto = valor % 1000
centena = resto//100
resto = resto % 100
dezena = resto//10
unidade = resto % 10
print("Valor invertido: ", unidade*1000 + dezena*100 + centena*10 + milhar)

# OUTRA OPCAO DE CODIGO

numero = int(input("Digite um numero inteiro de 4 digitos: "))

if 1000 <= numero <= 9999:
    milhar = numero // 1000
    centena = (numero // 100) % 100
    dezena = (numero // 100) % 10
    unidade = numero % 10

    numeroInvertido = unidade * 1000 + dezena * 100 + centena * 10 + milhar

    print("Número invertido: ", numeroInvertido)
else:
    print("Por favor, digite um número inteiro de 4 digitos: ")
