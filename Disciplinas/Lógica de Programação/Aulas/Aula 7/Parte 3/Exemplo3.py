# Variáveis com escopo local (juros compostos)

def calcula(base, taxa, duracao):
  final = base * (1 + taxa) ** duracao
  return final

b = float(input("Valor inicial: "))
t = float(input("Taxa de juros mensal: "))
d = float(input("Duração (meses): "))

res = calcula(b, t, d)
print(f"Valor no final do período: {res:.2f}") 