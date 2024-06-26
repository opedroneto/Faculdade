nTermos = int(input("Informe o numero de termos: "))
if nTermos <= 0: print("Numero de termos invalido")
else:
  soma = 0
  cont = 1
  numerador = 2
  denominador = 1
  while cont <= nTermos:
    soma = soma + numerador / denominador
    cont += 1
    numerador += 2
    denominador += 2
  print(f"Soma: {soma}")