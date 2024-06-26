'''

Construa um programa que le o tempo de um evento em segundos 
e o escreve decomposto em horas, minutos e segundos.

'''

tempoTotalSegundos = int(input("Informe o tempo do evento em segundos: "))

horas = tempoTotalSegundos // 3600
minutos = (tempoTotalSegundos % 3600) // 60
segundos = tempoTotalSegundos % 60

print(f"{tempoTotalSegundos} segundos equivalem a {
      horas} horas, {minutos} minutos e {segundos} segundos.")

# OUTRA OPCAO DE CODIGO

tempo = int(input("Informe o tempo do evento em segundos: "))
horas = tempo//3600
print("Horas: ", horas)
resto = tempo % 3600
minutos = resto//60
print("Minutos: ", minutos)
segundos = resto % 60
print("Segundos: ", segundos)
