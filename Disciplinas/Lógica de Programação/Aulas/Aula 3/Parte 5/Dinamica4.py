'''

Implemente um programa que leia o saldo médio de uma conta 
corrente, calcule e escreva o seu limite conforme a tabela abaixo.

Saldo Médio                     Limite
menor que R$ 500,00             não há limite
de R$ 500,00 a R$ 1000,00       8% do saldo médio
menor ou igual a R$ 1000,00     15% do saldo médio

'''

saldo = float(input("Informe o saldo médio: "))
if saldo < 500:
    print("Sem limite")
if saldo >= 500 and saldo <= 1000:
    print("Limite: ", saldo * 0.08)
if saldo > 1000:
    print("Limite: ", saldo * 0.15)
