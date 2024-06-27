# Função retornando valores para outras funções

def potencia(num):
  return num ** 2

def somaPotencias(a, b, c):
  return potencia(a) + potencia(b) + potencia(c)

val1 = int(input("Valor 1: "))
val2 = int(input("Valor 2: "))
val3 = int(input("Valor 3: "))
result = somaPotencias(val1, val2, val3)
print(f"Soma das potencias: {result}")