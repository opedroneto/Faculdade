'''

Codifique um programa que calcula o fatorial de um valor natural
Fatorial
0! = 1
1! = 1
2! = 2
3! = 2 x 3
4! = 2 x 3 x 4
5! = 2 x 3 x 4 x 5 

'''

valor = int(input("Informe um valor natural: "))
fat = 1
aux = 2
while aux <= valor:
  fat *= aux
  aux += 1
print(f"Fatorial: {fat}")