'''

Implemente um programa que leia a idade, altura e gênero de 
10 estudantes. O programa deve calcular e escrever:

  - Media de idade dos estudantes
  - Media de altura das meninas
  - Percentual de estudantes com mais de 20 anos
  - Altura do estudante mais velho

'''

cont = 0

while cont < 10:
    idade = int(input("Informe a sua idade: "))
    while idade <= 0 or idade > 120:
        print("> Idade inválida")
        idade = int(input("Informe novamente a sua idade: "))

    altura = float(input("Informe a sua altura: "))
    while altura <= 0 or altura > 2.5:
        print("> Altura inválida")
        altura = float(input("Informe novamente a sua altura: "))

    genero = int(
        input("Informe o seu genero: 1 para feminino e 2 para masculino: "))
    while genero != 1 and genero != 2:
        print("Gênero inválido. Informe 1 ou 2")
        genero = int(
            input("Informe novamente o seu genero: 1 para feminino e 2 para masculino: "))

    soma = soma + idade
    cont += 1

print(f"Média de idade dos estudantes: {soma / cont}")
