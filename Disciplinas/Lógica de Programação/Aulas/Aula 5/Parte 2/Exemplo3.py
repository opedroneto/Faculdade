import random

soma = 0
maior = 0
for cont in range(10):
    alt = random.uniform(1.5, 2.1)
    soma += alt
    if alt > maior:
        maior = alt

media = soma / 10
print(f"Media: {media:.3f}")
print(f"Maior altura: {maior}")
