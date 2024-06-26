'''

Um ano é bissexto se
  - ...for divisível por 4
  - ...mas não por 100, a menos que seja divisível por 400
Escreva um programa que recebe como entrada um ano e determina 
se ele é bissexto ou não

'''

ano = int(input("Informe o ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Ano Bissexto")
else:
    print("Não é Bissexto")
