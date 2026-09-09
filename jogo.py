import random

print("Jogo de adivinhação - Você tem 7 tentativas")
print("Tente adivinhar o número que estou pensando entre 1 e 100")

numero_secreto = random.randint(1, 100)
contador = 7
acertou = False

while contador > 0:
    print(f"Você tem {contador} tentativas restantes")

    tentativa = int(input("Digite o seu palpite: "))
    contador -= 1

    if tentativa == numero_secreto:
        print("Número correto!", numero_secreto)
        acertou = True
        break

    elif tentativa > numero_secreto:
        print("Seu número é maior que o número secreto")

    else:
        print("Seu número é menor que o número secreto")

if not acertou:
    print("Você errou. O número secreto era:", numero_secreto)
else:
    print("Você acertou. Na tentativa:", 7 - contador)
