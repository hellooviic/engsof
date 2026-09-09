import random

print ("Jogo de adivinhação - Você tem 7 tentaivas")
print("Tente adivinhar o número que estou pensando entre 1 a 100")

numero_secreto = random.randint(1, 100)
contador = 7
acertou = False


while contador > 0:
    # print(f"Voce tem {contador} tentativas restantes")
    contador -= 1
    tentativa = int(input("Digite o seu palpite: "))
    if tentativa == numero_secreto:
        print("Número correto!", numero_secreto)
        acertou = True
        break    
    elif tentativa > numero_secreto:
        print("Seu número é menor que o número secreto")    
    else: 
        print("Seu número é maior que o número secreto")    

if not acertou:
    print("Você errou. O número secreto era: ", numero_secreto)
else:
    print("Você acertou. Na tentativa: ", 7 - contador + 1)
