"""
Exemplos:

5!
n!/((n-p)!p!)
"""

import math

a = 5
n = 3
p = 2

resultado = math.factorial(a)
print(resultado)

resultado = math.factorial(n)/(math.factorial(n-p) * math.factorial(p))
print(resultado)
