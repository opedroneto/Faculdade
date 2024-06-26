'''

Elabore um programa que leia um número inteiro de 4 digitos (garanta isso).
A seguir o programa deve determinar se o numero lido é capicua. Um número é 
capicua quando lido da esquerda para a direita ou da direita para a esquerda 
representa sempre o mesmo valor, como por exemplo 6446.

'''

numero = int(input("Informe um numero inteiro de 4 digitos: "))
if numero < 1111 or numero > 9999:
    print("Numero invalido, nao tem 4 digitos.")
else:
    milhar = numero // 1000
    resto = numero % 1000
    centena = resto // 100
    resto = resto % 100
    dezena = resto // 10
    unidade = resto % 10
    invertido = unidade * 1000 + dezena * 100 + centena * 10 + milhar
    print("Valor invertido: ", invertido)
    if numero == invertido:
        print("Capicua")
    else:
        print("Nao eh capicua")
