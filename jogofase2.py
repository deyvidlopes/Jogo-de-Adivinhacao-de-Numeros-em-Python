import random

numero_secreto = random.randint(0, 10)

print("Você tem uma única chance para adivinhar um número entre 0 e 10.")

palpite = int(input("Qual é o seu palpite? "))

if palpite == numero_secreto:
    print("Parabéns! Você acertou o número secreto.")
else:
    print(f"Você errou. O número secreto era {numero_secreto}.")
print("Fim de jogo!")

