soma = 0
num = int(input("Num: "))
for cont in range(1, num+1):
  soma += cont
  print(f"{cont}: {soma}")
print(f"Somatório: {soma}")