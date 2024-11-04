from random import randint

pontuacao = 1000

print("***** Jogo da adivinhação *****")
print("******************************")

nome = input('Digite seu nome: ')
print(f"Bem vindo {nome}! Eu sou o computador, que tal tentar adivinhar o numero que pensei? ")

while True:
    dificuldade = int(input(f"Em qual dificuldade voce deseja jogar? (1 a 3)"))
    if dificuldade in [1,2,3]:
        break
    else:
        print("É necessário escolher uma dificuldade válida!")

num_tentativas = 5 - dificuldade
tente = num_tentativas
sorteio = randint(1, 5) + dificuldade
entre = 1,  5 + dificuldade
tentativa = 1

while num_tentativas >= 1:
    print(f"Tentativa {tentativa} de {tente}. Sua pontuaçao atual é {pontuacao}.")
    print(f"O numero estará entre {entre}")
   
    chute = int(input("Qual numero pensei? "))

    acertou = chute == sorteio

    if acertou:
        print(f"voce acertou, parabens!!! Sua pontuação final foi {pontuacao}")
        break
    else:
        print(f"Que pena, você errou:(")

    num_tentativas-=1
    tentativa+=1
    if dificuldade == 1 :
        pontuacao -=250
    elif dificuldade == 2:
        pontuacao -=333.333
    elif dificuldade == 3:
        pontuacao -=500

    if num_tentativas == 0:
      print(f"Infelizmente voce nao acertou, o numero que pensei foi {sorteio} e sua pontuação final foi {pontuacao}")