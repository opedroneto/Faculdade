'''

Jogo Pedra Papel Tesoura

'''

import random

jogador = input("Sua escolha Pedra, Papel, Tesoura? ")
computador = random.choice(["Pedra", "Papel", "Tesoura"])
print(f"Computador escolheu: {computador}")

if jogador == computador:
    print(f"Empate!")
elif jogador == "Pedra":
    if computador == "Tesoura":
        print("Pedra quebra Tesoura! Você venceu!")
    else:
        print("Papel cobre Pedra! Você perdeu!")
elif jogador == "Papel":
    if computador == "Pedra":
        print("Papel cobre Pedra! Você venceu!")
    else:
        print("Tesoura corta Papel! Você perdeu!")
elif computador == "Papel":
    print("Tesoura corta Papel! Você venceu!")
else:
    print("Pedra quebra Tesoura! Você perdeu!")
