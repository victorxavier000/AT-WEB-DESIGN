def jogo_adivinhacao():
    numero_secreto = 67
    tentativas = 0

    print("Jogo de Adivinhação ")
    print("Tente adivinhar o número secreto entre 1 e 100!")

    while True:
        palpite = int(input("Seu palpite: "))
        tentativas += 1

        if palpite < numero_secreto:
            print("Muito baixo! Tente um número maior.")
        elif palpite > numero_secreto:
            print("Muito alto! Tente um número menor.")
        else:
            print(f"Parabéns! Você acertou o número {numero_secreto}!")
            print(f"Número total de tentativas: {tentativas}")
            break


