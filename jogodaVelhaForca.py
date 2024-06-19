# Lauro Dariva Ferneda - RA: 1136899

import os, time
os.system ("cls")


print("Bem vindo ao VELHO JOGO DA FORCA!!! ୧(ᵔᴗᵔ)୨")
time.sleep(4)
os.system("cls")
print("Neste jogo será necessário ao menos dois jogadores, então nem tente testa-lo sozinho(a), ok? (งᗒ﹏ᗕ)ง ")
time.sleep(6)
os.system("cls")
print("Então vamos para as regras!!! (～╹⌔╹)～")
time.sleep(4)
os.system("cls")
regras= input("""REGRAS: 
1- O primeiro jogador deve escolher uma palavra enquanto o outro fica de costas ou de olhos fechados. ᕙ(￫ ‸ ￩)ᕗ
2- Após isso o segundo jogador deverá tentar adivinha-lá, letra por LETRA! (☉ □ ☉)
3- Caso não consiga em 6 (seis) tentativas você irá para a FORCA. (๏ ̪  ๏)
      
(PRESSIONE ENTER PARA CONTINUAR)
""")
os.system ("cls")
competidor = input("Nome do Competidor: ")
desafiante = input("Nome do Desafiante: ")
palavraJogador1 = input("Escolha uma palavra: ")
os.system("cls")

letrasPalavraj1 = []

chances = 6

dica1 = input("Dica1: ")
dica2 = input("Dica2: ")
dica3 = input("Dica3: ")
os.system("cls")

vitoria = False

while True:

    for letra in palavraJogador1:
        if letra.lower() not in letrasPalavraj1:
            print("_", end=" ")
        else:
            print(letra, end=" ")
    menu = input("""
(1) Para Jogar:
(2) Para Dica:                  
""")
    os.system("cls")
    if menu == "1":
        pass
    if menu == "2":
        dica = input("Precione 1 para dica1, 2 para dica2 e 3 para dica3: ")
        if dica == "1":
            print(f"A primeira dica é: {dica1}")
            time.sleep(2)
            os.system("cls")
        if dica == "2":
            print(f"A segunda dica é: {dica2}")
            time.sleep(2)
            os.system("cls")
        if dica == "3":
            print(f"A terceira dica é: {dica3}")
            time.sleep(2)
            os.system("cls")

    print(f"Você tem {chances} chances")

    jogatina = input("Escolha uma letra: ")
    os.system("cls")

    letrasPalavraj1.append(jogatina.lower())

    if jogatina.lower() not in palavraJogador1.lower():

        chances -= 1
        print(f"A letra {letrasPalavraj1[-1]} não está na palavra")
        time.sleep(2)
        os.system("cls")
        print(f"Agora você tem {chances} chances")
    
    vitoria = True

    for letra in palavraJogador1:
        if letra.lower() not in letrasPalavraj1:
            vitoria = False
    if chances == 0 or vitoria:
        break


os.system ("cls")

if vitoria:
    print(f"""PARABÉNS {desafiante} VOCÊ É O(A) VERDADEIRO(A) VELHO(A) FORCA ୧(*◒*)୨
A palavra era {palavraJogador1} o tempo todo!""")
    time.sleep(4)
    os.system ("cls")
    exit()
else:
    print(f"""Nem sei porque confiei em você {desafiante}, agora nunca saberemos a palavra (o̧̥̻ ♨ o̧̥̻)
{competidor}, você venceu...""")
    time.sleep(6)
    os.system ("cls")
    exit()