'''

Implemente um programa que calcula a soma do n primeiros termos da serie a seguir:
                            1 + 1/2 + 1/3 + 1/4 + 1/5 + ...

'''

nTermos = int(input("Informe a quantidade de termos: "))
if nTermos <= 0: print("N° de termos inválido")
else:
  soma = 0
  cont = 1
  while cont <= nTermos:
    soma = soma + 1/cont
    cont += 1
  print(f"Soma: {soma}") 
