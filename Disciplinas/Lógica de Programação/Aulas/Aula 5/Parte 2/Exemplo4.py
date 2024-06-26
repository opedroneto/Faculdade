'''

Foram entrevistados 50 estudantes de Engenharia. De cada estudante foram coletados
os seguintes dados: idade, semestre e curso.
O programa deve "ler" (sortear) os dados dos estudantes, calcular e escrever:
  - media de idade dos estudantes
  - curso do aluno mais velho
  - quantidade de alunos que estão no 5° semestre

'''

import random

somaIdades = 0
cursoMaisVelho = " "
idadeMaisVelho = 0
qtdAlunos5Semestre = 0

for cont in range(50):  # 50 estudantes
    # sorteio
    idade = random.randint(18, 60)
    curso = random.choice(
        ["Eng. Civil", "Eng. Mec", "Eng. Quim", "Eng. Prod"])
    semestre = random.randint(1, 10)
    print(f"Idade: {idade} Curso: {curso} Semestre: {semestre}")
    # Coleta de estatisticas
    # Media de idades: é necessario somar as idades
    somaIdades += idade
    # Curso do aluno mais velho
    if idade > idadeMaisVelho:
        idadeMaisVelho = idade
        cursoMaisVelho = curso
    # Total de alunos no 5° semestre
    if semestre == 5:
        qtdAlunos5Semestre += 1

mediaIdades = somaIdades // 50
print(f"Media de idades: {mediaIdades}")
print(f"Curso do aluno mais velho ({idadeMaisVelho} anos): {cursoMaisVelho}")
print(f"Total de alunos no 5° semestre: {qtdAlunos5Semestre}")
