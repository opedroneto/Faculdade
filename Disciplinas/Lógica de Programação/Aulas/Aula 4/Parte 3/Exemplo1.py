'''

Número de dias em um mês específico
- Dado um mês qualquer (1-12), exibir a quantidade total de dias
- Obs: sem considerar anos bissextos
Meses podem ter 28, 30 ou 31 dias

'''

mes = int(input("Mês: "))

if mes == 2:
    dias = 28
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    dias = 30
else:
    dias = 31
print(f"Total de dias: {dias}")
