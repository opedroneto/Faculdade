# Cálculo de raízes de equação quadratica

import math

a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))

delta = b * b - 4 * a * c

if delta < 0 :
  print("Não há raizes reais")
else :
  if delta == 0:
    x = - b / (2 * a)
    print(f"Raiz é {x}")
  else:
    x1 = (- b + math.sqrt(delta)) / (2 * a)
    x2 = (- b - math.sqrt(delta)) / (2 * a)
    print(f"Raízes são {x1} e {x2}")