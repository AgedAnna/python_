import random

palavras = ["maçã", "pera", "morango"]

palavra_secreta = random.choice(palavras)
palavra_oculta = ["_" for _ in palavra_secreta]
tentativas_erradas = 0
max_tentativas = 5

print("Bem-vindo ao jogo da palavra secreta!")
print("A palavra secreta possui: ", " ".join(palavra_oculta))

while tentativas_erradas < max_tentativas and "_" in palavra_oculta:
    letra = input("Digite uma letra: ").lower()

    if letra in palavra_secreta:
        for i, char in enumerate(palavra_secreta):
            if char == letra:
                palavra_oculta[i] = letra
        print("Correto!")
    else:
        tentativas_erradas += 1
        print(f"Errado! Você tem {max_tentativas - tentativas_erradas} tentativas restantes.")

    print(" ".join(palavra_oculta))

if "_" not in palavra_oculta:
    print("Parabéns! Você adivinhou a palavra secreta!")
else:
    print(f"Você perdeu! A palavra secreta era '{palavra_secreta}'.")
