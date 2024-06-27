# Uso de parametros default

def calcula(base, taxa=0.1, duracao=12):
  final = base * (1+taxa) ** duracao
  return final

b = float(input("Valor inicial: "))
#t = float(input("Taxa de juros mensal: "))
#d = float(input("Duração (meses): "))

res = calcula(b)
print(f"Valor no final do período: {res:.2f}")