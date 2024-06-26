'''

Aprovação de aluno por nota e frequencia, com exame

- Aluno realiza 3 provas com o mesmo peso
- Grau 1 (G1) é calculado pela média aritmética das provas
- Aluno precisa estar presente em 75% das aulas, caso contrário estará reprovado por faltas

- Se o G1 for igual ou superior a 7, o aluno estará aprovado em G1
- Se o G1 for inferior a 4, o aluno estará reprovado
- Se o G1 for inferior a 7, o aluno deverá realizar um exame (G2)
  - Se a média entre G1 e a nota do exame G2 for igual ou superior a 5, o aluno estará 
    aprovado em grau 2
  - Se a média for inferior a 5, o aluno estará reprovado em grau 2

'''

prova1 = float(input("Informe a nota da Prova 1: "))
prova2 = float(input("Informe a nota da Prova 2: "))
prova3 = float(input("Informe a nota da Prova 3: "))

frequencia = float(input("Frequência: "))

g1 = (prova1 + prova2 + prova3) / 3

print(f"Média G1: {g1}")

if frequencia < 75:
  print(f"Reprovado por faltas: {frequencia}")
else:
  if g1 >= 7:
    print(f"Aprovado por média: {g1}")
  else:
    if g1 < 4:
      print(f"Reprovado por média: {g1}")
    else:
      # Em exame (G2)
      g2 = float(input("G2: "))
      mediaFinal = (g1 + g2) / 2
      if mediaFinal >= 5:
        print(f"Aprovado em G2: {mediaFinal}")
      else:
        print(f"Reprovado em G2: {mediaFinal}")