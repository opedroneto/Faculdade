# Variaveis para armazenar as temperaturas de cada mes 
tempJan = 0
tempFev = 0
tempMar = 0
tempAbr = 0
tempMai = 0
tempJun = 0
tempJul = 0
tempAgo = 0
tempSet = 0
tempOut = 0
tempNov = 0
tempDez = 0

# Variaveis auxiliares
somaTemperaturas = 0
mesesEscaldantes = 0

# Repeticao para coletar dados para cada mes
for i in range(1, 13):
  mes = int(input(f"Informe o mês: "))
  if mes < 1 or mes > 12:
    print("Erro: O mes deve ser um numero inteiro entre 1 e 12.")
    continue

  tempMaxima = float(input(f"Informe a temperatura máxima do mês (em C°): "))
  if tempMaxima < -60 or tempMaxima > 50:
    print("Erro: A temperatura deve estar entre -60º e 50° graus Celsius.")
    continue

  # Atribui a temperatura ao mes
  if mes == 1:
    tempJan = tempMaxima
  elif mes == 2:
    tempFev = tempMaxima
  elif mes == 3:
    tempMar = tempMaxima
  elif mes == 4:
    tempAbr = tempMaxima
  elif mes == 5:
    tempMai = tempMaxima
  elif mes == 6:
    tempJun = tempMaxima
  elif mes == 7:
    tempJul = tempMaxima
  elif mes == 8:
    tempAgo = tempMaxima
  elif mes == 9:
    tempSet = tempMaxima
  elif mes == 10:
    tempOut = tempMaxima 
  elif mes == 11:
    tempNov = tempMaxima
  elif mes == 12:
    tempDez = tempMaxima 

  somaTemperaturas += tempMaxima

  # Verificar se a temperatura e escaldante
  if tempMaxima > 33:
    mesesEscaldantes += 1

# Calcular temperatura media maxima anual
tempMediaMaximaAnual = somaTemperaturas / 12

# Mes mais escaldante
tempMaxima = tempJan
mesMaisEscaldante = 1
if tempFev > tempMaxima:
  tempMaxima = tempFev
  mesMaisEscaldante = 2
if tempMar > tempMaxima:
  tempMaxima = tempMar
  mesMaisEscaldante = 3
if tempAbr > tempMaxima:
  tempMaxima = tempAbr
  mesMaisEscaldante = 4
if tempMai > tempMaxima:
  tempMaxima = tempMai
  mesMaisEscaldante = 5
if tempJun > tempMaxima:
  tempMaxima = tempJun
  mesMaisEscaldante = 6
if tempJul > tempMaxima:
  tempMaxima = tempJul
  mesMaisEscaldante = 7
if tempAgo > tempMaxima:
  tempMaxima = tempAgo
  mesMaisEscaldante = 8
if tempSet > tempMaxima:
  tempMaxima = tempSet
  mesMaisEscaldante = 9
if tempOut > tempMaxima:
  tempMaxima = tempOut
  mesMaisEscaldante = 10
if tempNov > tempMaxima:
  tempMaxima = tempNov
  mesMaisEscaldante = 11
if tempDez > tempMaxima:
  tempMaxima = tempDez
  mesMaisEscaldante = 12  

# Mes menos quente
tempMinima = tempJan
mesMenosQuente = 1
if tempFev < tempMinima:
  tempMinima = tempFev
  mesMenosQuente = 2
if tempMar < tempMinima:
  tempMinima = tempMar
  mesMenosQuente = 3
if tempAbr < tempMinima:
  tempMinima = tempAbr
  mesMenosQuente = 4
if tempMai < tempMinima:
  tempMinima = tempMai
  mesMenosQuente = 5
if tempJun < tempMinima:
  tempMinima = tempJun
  mesMenosQuente = 6
if tempJul < tempMinima:
  tempMinima = tempJul
  mesMenosQuente = 7
if tempAgo < tempMinima:
  tempMinima = tempAgo
  mesMenosQuente = 8
if tempSet < tempMinima:
  tempMinima = tempSet
  mesMenosQuente = 9
if tempOut < tempMinima:
  tempMinima = tempOut
  mesMenosQuente = 10
if tempNov < tempMinima:
  tempMinima = tempNov
  mesMenosQuente = 11
if tempDez < tempMinima:
  tempMinima = tempDez
  mesMenosQuente = 12

# Tranformar o numero do mes em nome do mes
if mesMaisEscaldante == 1:
  mesMaisEscaldanteNome = "Janeiro"
elif mesMaisEscaldante == 2:
  mesMaisEscaldanteNome = "Fevereiro"
elif mesMaisEscaldante == 3:
  mesMaisEscaldanteNome = "Março"
elif mesMaisEscaldante == 4:
  mesMaisEscaldanteNome = "Abril"
elif mesMaisEscaldante == 5:
  mesMaisEscaldanteNome = "Maio"
elif mesMaisEscaldante == 6:
  mesMaisEscaldanteNome = "Junho"
elif mesMaisEscaldante == 7:
  mesMaisEscaldanteNome = "Julho"
elif mesMaisEscaldante == 8:
  mesMaisEscaldanteNome = "Agosto"
elif mesMaisEscaldante == 9:
  mesMaisEscaldanteNome = "Setembro"
elif mesMaisEscaldante == 10:
  mesMaisEscaldanteNome = "Outubro"
elif mesMaisEscaldante == 11:
  mesMaisEscaldanteNome = "Novembro"
elif mesMaisEscaldante == 12:
  mesMaisEscaldanteNome = "Dezembro"

if mesMenosQuente == 1:
  mesMenosQuenteNome = "Janeiro"
elif mesMenosQuente == 2:
  mesMenosQuenteNome = "Fevereiro"
elif mesMenosQuente == 3:
  mesMenosQuenteNome = "Março"
elif mesMenosQuente == 4:
  mesMenosQuenteNome = "Abril"
elif mesMenosQuente == 5:
  mesMenosQuenteNome = "Maio"
elif mesMenosQuente == 6:
  mesMenosQuenteNome = "Junho"
elif mesMenosQuente == 7:
  mesMenosQuenteNome = "Julho"
elif mesMenosQuente == 8:
  mesMenosQuenteNome = "Agosto"
elif mesMenosQuente == 9:
  mesMenosQuenteNome = "Setembro"
elif mesMenosQuente == 10:
  mesMenosQuenteNome = "Outubro"
elif mesMenosQuente == 11:
  mesMenosQuenteNome = "Novembro"
elif mesMenosQuente == 12:
  mesMenosQuenteNome = "Dezembro"

# Imprimir os resultados
print(f"Temperatura média máxima anual: {tempMediaMaximaAnual:.2f}°C")
print(f"Quantidade de meses escaldantes: {mesesEscaldantes} meses")
print(f"Mês mais escaldante do ano: {mesMaisEscaldanteNome}")
print(f"Mês menos quente do ano: {mesMenosQuenteNome}")