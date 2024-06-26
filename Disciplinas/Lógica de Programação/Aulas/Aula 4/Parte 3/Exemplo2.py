'''

Índice de Massa Corporal (IMC)
- Cálculo: imc = peso / altura**2
- Faixas definem categorias de peso

IMC                 CLASSIFICAÇÃO
Abaixo de 18,6      Abaixo do peso
Entre 18,6 e 24,9   Peso ideal
Entre 25 e 29,9     Sobrepeso
Entre 30 e 34,9     Obesidade grau 1
Entre 35 e 39,9     Obesidade grau 2 (severa)
Acima de 39,9       Obesidade grau 3 (mórbida)

'''

altura = float(input("Informe a altura: "))
peso = float(input("Informe o peso: "))
imc = peso / altura**2

print(f"Seu IMC é {imc}")

if imc < 18.6:
    print("Abaixo do peso")
elif 18.6 <= imc <= 24.9:
    print("Peso ideal")
elif 25 <= imc <= 29.9:
    print("Sobrepeso")
elif 30 <= imc <= 34.9:
    print("Obesidade Grau I")
elif 35 <= imc <= 39.9:
    print("Obesidade Grau II")
else:
    print("Obesidade Grau III")
