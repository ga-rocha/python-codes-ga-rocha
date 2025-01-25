def jogo_adivinhar_palavra():
    palavra_secreta = "Eu sou o melhor"  # Palavra secreta a ser adivinhada
    letras_adivinhadas = []  # Lista para armazenar as letras adivinhadas
    tentativas = 0  # Contador de tentativas

    print("Bem-vindo ao jogo da palavra secreta!")
    print(f"A palavra secreta tem {len(palavra_secreta)} letras.")
    
    while True:
        # Mostrar o progresso do jogador
        progresso = ""
        for letra in palavra_secreta:
            if letra in letras_adivinhadas:
                progresso += letra
            else:
                progresso += "*"
        print(f"\nPalavra: {progresso}")

        # Checar se o jogador já adivinhou a palavra
        if progresso == palavra_secreta:
            print(f"\nParabéns! Você adivinhou a palavra secreta: {palavra_secreta}")
            print(f"Número de tentativas: {tentativas}")
            break

        # Solicitar uma letra do jogador
        letra = input("Digite uma letra: ").lower()

        # Validar a entrada do usuário
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, digite apenas uma letra.")
            continue

        tentativas += 1

        # Verificar se a letra está na palavra secreta
        if letra in palavra_secreta:
            if letra not in letras_adivinhadas:
                letras_adivinhadas.append(letra)
                print(f"A letra '{letra}' está na palavra secreta!")
            else:
                print(f"Você já adivinhou a letra '{letra}'.")
        else:
            print(f"A letra '{letra}' NÃO está na palavra secreta.")

# Iniciar o jogo
jogo_adivinhar_palavra()
