# import random

# numero_secreto = random.randint(0, 10)

# print("Você tem uma única chance para adivinhar um número entre 0 e 10.")

# palpite = int(input("Qual é o seu palpite? "))

# if palpite == numero_secreto:
#     print("Parabéns! Você acertou o número secreto.")
# else:
#     print(f"Você errou. O número secreto era {numero_secreto}.")
# print("Fim de jogo!")

import random

def jogo_numero_secreto():
    print("Bem-vindo ao Jogo do Número Secreto!")
            
    while True:
        try:
            nivel = int(input("Escolha um nível de dificuldade:\n1 - Fácil (30 tentativas)\n2 - Médio (15 tentativas)\n3 - Difícil (5 tentativas)\nDigite o número do nível: "))
            if nivel not in [1, 2, 3]:
                print("Escolha de nível inválida. Por favor, escolha 1, 2 ou 3.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    if nivel == 1:
        numero_secreto = random.randint(1, 50)
        max_tentativas = 30
        print(f"Você escolheu o nível Fácil. Tente adivinhar o número entre 1 e 50.")
    elif nivel == 2:
        numero_secreto = random.randint(1, 50)
        max_tentativas = 15
        print(f"Você escolheu o nível Médio. Tente adivinhar o número entre 1 e 50.")
    else: #nivel == 3
        numero_secreto = random.randint(1, 50)
        max_tentativas = 5
        print(f"Você escolheu o nível Difícil. Tente adivinhar o número entre 1 e 50.")
    
    tentativas_usadas = 0

    while tentativas_usadas < max_tentativas:
        try: 
            chute = int(input(f"Tentativa {tentativas_usadas + 1}/{max_tentativas}: Digite seu palpite: "))
            
            if chute == numero_secreto:
                print(f"Parabéns! Você acertou o número secreto ({numero_secreto}) em {tentativas_usadas + 1} tentativas!")
                break
            elif chute < numero_secreto:
                print("Seu chute foi muito baixo. Tente um número maior.")
            else:
                print("Seu chute foi muito alto. Tente um número menor.")
                
            tentativas_usadas += 1

        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    if tentativas_usadas >= max_tentativas and chute != numero_secreto:
        print(f"Suas tentativas acabaram. O número secreto era {numero_secreto}. Mais sorte na próxima vez!")

if __name__ == "__main__":
    jogo_numero_secreto()
