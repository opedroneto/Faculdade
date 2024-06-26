'''

Faça um programa que leia o horario de inicio de um jogo, em horas e minutos, e o 
horário de fim desse jogo, tambem em hora e minutos. Sabendo que a duração maxima do 
jogo é de 24 horas, determine o tempo de duração do jogo em horas e minutos.

'''

horaInicio = int(input("Informe a hora inicial do jogo: "))
minutoInicio = int(input("Informe o minuto inicial do jogo: "))
horaFinal = int(input("Informe a hora final do jogo: "))
minutoFinal = int(input("Informe o minuto final do jogo: "))

horarioInicial = horaInicio * 60 + minutoInicio
horarioFinal = horaFinal * 60 + minutoFinal

if horarioInicial < horarioFinal:
    duracao = horarioFinal - horarioInicial
else:
    duracao = 24 * 60 - horarioInicial + horarioFinal

print("Horas: ", duracao//60)
print("Minutos: ", duracao % 60)
