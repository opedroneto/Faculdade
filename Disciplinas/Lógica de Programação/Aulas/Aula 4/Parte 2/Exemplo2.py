'''

Determinar conceito de um aluno em função da sua nota

NOTA        CONCEITO 
>= 90       A
80 <= 90    B
70 <= 80    C
60 <= 70    D
< 60        F

'''

nota = int(input("Informe a nota: "))

if nota >= 90:
  print("Conceito A")
elif 80 <= nota <= 90:
  print("Conceito B")
elif 70 <= nota <= 80:
  print("Conceito C")
elif 60 <= nota <= 70:
  print("Conceito D")
else:
  print("Conceito F")