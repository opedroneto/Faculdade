'''

Faça um programa que converte de Fahrenheit para graus Celsius. O programa deve ler
um valor em Fahrenheit, converter e escrever o valor correspondente em Celsius. Para realizar 
a conversão usa a fórmula c = 5/9 (f - 32).

'''

print("Informe o valor em Fahrenheit: ")
f = float(input())
c = 5/9 * (f-32)
print("Celsius: ", c)
