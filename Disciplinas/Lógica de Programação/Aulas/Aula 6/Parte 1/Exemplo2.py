'''

Codifique um programa que escreva os divisores de um numero.
Divisores
1
2 -> 1 e 2
3 -> 1 3 3
4 -> 1, 2 e 4
5 -> 1 e 5
6 -> 1, 2, 3 e 6 

'''

valor = int(input("Informe um valor natural: "))
d = 1
while d <= 10:
  if valor % d == 0: print(d, " divide ", valor)
  d += 1