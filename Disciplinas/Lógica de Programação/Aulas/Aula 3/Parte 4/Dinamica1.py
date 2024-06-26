'''

Implemente um programa que determina o preço de venda dos produtos de uma 
loja conforme o preço de custo desses produtos. O programa deve ler o preço 
de custo e calcular o valor de venda conforme a tabela abaixo.

preço unitario de custo           preço de venda
valor abaixo de R$ 10,00          lucro de 70%
de R$ 10,00 a menos de R$ 30,00   lucro de 50%
de R$ 30,00 a menos de R$ 50,00   lucro de 40%
valor acima ou igual a R$ 50,00   lucro de 30%

'''

preco = float(input("Informe o preço de custo: "))
if preco < 0:
    print("Valor invalido.")
else:
    if preco < 10:
        venda = preco * 1.7
    if preco >= 10 and preco < 30:
        venda = preco * 1.5
    if preco >= 30 and preco < 50:
        venda = preco * 1.4
    if preco >= 50:
        venda = preco * 1.3
    print("Preço de venda: ", venda)
