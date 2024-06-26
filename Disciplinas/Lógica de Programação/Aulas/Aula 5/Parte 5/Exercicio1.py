'''

Implementar o Jogo da Adivinhação, onde o objetivo é adivinhar um número
sorteado pelo computador:
  - No início, o computador sorteia um número entre 1 e 100
  - O jogador tem 10 chances para adivinhar o número
  - A cada chance, o computador deve informar se o número é maior, menor ou igual ao sorteado
  - Se for igual, o jogo termina e o jogador é informado da vitória
  - Quando acabarem as chances, o jogo também termina e o jogador é informado da derrota

'''

import random

sorteado = random.randint(1, 100)
# print(f"Sorteado: {sorteado}")

acertou = False

for tent in range(1, 11):
    print(f"Tentativa {tent}: ", end="")
    num = int(input())
    if num < sorteado:
        print("Tente um número maior")
    elif num > sorteado:
        print("Tente um número menor")
    else:
        acertou = True
        break

if acertou:
    print("Parabéns, você acertou!")
else:
    print(f"Que pena, você perdeu.. O número era {sorteado}")
