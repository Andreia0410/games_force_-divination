import random


def jogar():
    mensagem_de_abertura()
    palavra_secreta = leva_palavra_secreta()

    letras_acertadas = inicializa_letras_acertas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    tentativa = 0

    while (not enforcou and not acertou):
        chute = chute_do_jogador()

        if (chute in palavra_secreta):
            chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            tentativa += 1
            desenha_forca(tentativa)
        enforcou = tentativa == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        menssagem_vencedora()
    else:
        menssagem_perdedora(palavra_secreta)


def desenha_forca(tentativa):
    print("  _______     ")
    print(" |/      |    ")

    if(tentativa == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(tentativa == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(tentativa == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(tentativa == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(tentativa == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(tentativa == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (tentativa == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def menssagem_vencedora():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def menssagem_perdedora(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute.upper() == letra.upper()):
            letras_acertadas[index] = letra
        index += 1


def chute_do_jogador():
    chute = input('  Chute uma letra ? ')
    chute = chute.strip().upper()
    return chute


def inicializa_letras_acertas(palavra):
    lista = ["_" for letra in palavra]
    return lista


def mensagem_de_abertura():
    print('*'*35)


mensagem_de_abertura()
print("     Bem-Vindo ao jogo da Forca!  ")
mensagem_de_abertura()


def leva_palavra_secreta():
    arquivo = open("palavra.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return(palavra_secreta)


if (__name__ == "__main__"):
    jogar()
