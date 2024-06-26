'''

Cálculo de salário líquido
  - Entradas: salário bruto e total de dependentes
  - Saídas:
    - Desconto do INSS
    - Desconto do IRRF (imposto retido na fonte)
    - Salário líquido

'''

salarioBruto = float(input("Salário Bruto: R$ "))
dependentes = int(input("Total dependentes: "))

# De acordo com a faixa de salário, determina
# a alíquota do INSS e parcela a deduzir
if salarioBruto < 1212.01:
    aliquotaInss = 0.075  # 7,5%
    parcelaInss = 0
    # inss = salarioBruto * 0.075
elif salarioBruto <= 2427.35:
    aliquotaInss = 0.09  # 9%
    parcelaInss = 18.18
    # inss = salarioBruto * 0.09 - 18.18
elif salarioBruto <= 3641.03:
    aliquotaInss = 0.12  # 12%
    parcelaInss = 91
    # inss = salarioBruto * 0.12 - 91
else:
    aliquotaInss = 0.14  # 14%
    parcelaInss = 163.82
    # inss = salarioBruto * 0.14 - 163.82

inss = salarioBruto * aliquotaInss - parcelaInss

# Verifica se desconto do INSS não passou do teto da última faixa
if inss > 828.39:
    inss = 828.39  # nesse caso, limita em 828.39

print("INSS: ", inss)

# Base para cálculo do IRRF
baseIrrf = salarioBruto - inss - 189.59 * dependentes

print(f"Base para cálculo IRRF: {baseIrrf:.2f}")

# De acordo com a faixa de salário, determina a alíquota do imposto e a parcela a deduzir
if baseIrrf <= 1903.98:
    aliquotaIrrf = 0
    parcelaIrrf = 0
elif baseIrrf <= 2826.65:
    aliquotaIrrf = 0.075  # 7,5%
    parcelaIrrf = 142.80
elif baseIrrf <= 3751.05:
    aliquotaIrrf = 0.15  # 15%
    parcelaIrrf = 354.80
elif baseIrrf <= 4664.68:
    aliquotaIrrf = 0.225  # 22,5%
    parcelaIrrf = 636.16
else:
    aliquotaIrrf = 0.275  # 22,5
    parcelaIrrf = 869.36

# IRRF é a alíquota (%) aplicada à base de cálculo, subtraída da parcela a deduzir
irrf = baseIrrf * aliquotaIrrf - parcelaIrrf

print("Imposto retido na fonte: ", irrf)

# Salário líquido é o bruto, subtraído do INSS e do IRRF calculado
liquido = salarioBruto - inss - irrf

print("Salário líquido: ", liquido)
